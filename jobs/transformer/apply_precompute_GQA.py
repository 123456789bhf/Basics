import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def precompute_freqs_cis(dim, max_seq_len):
    freqs = torch.arange(0, dim, 2).float() / dim
    inv_freq = 1.0 / (10000 ** freqs)
    pos_seq = torch.arange(0, max_seq_len).float()

    sin_inp = torch.einsum("i,j->ij", pos_seq, inv_freq)
    emb = torch.cat((sin_inp.sin(), sin_inp.cos()), dim=-1)
    return emb  # Shape: (max_seq_len, dim)

def apply_rotary_pos_emb(x, freqs_cis):
    # Apply rotary position embedding to the query/key tensors
    x = x.view(*x.shape[:-1], 2, -1)
    x1, x2 = x.unbind(dim=-2)
    return torch.cat([x1 * freqs_cis.cos() - x2 * freqs_cis.sin(),
                      x1 * freqs_cis.sin() + x2 * freqs_cis.cos()], dim=-1)

def repeat_kv(x: torch.Tensor, n_rep: int) -> torch.Tensor:
    """Repeats K and V heads to match the number of Q heads."""
    bs, slen, n_kv_heads, head_dim = x.shape
    if n_rep == 1:
        return x
    return (
        x[:, :, :, None, :]
        .expand(bs, slen, n_kv_heads, n_rep, head_dim)
        .reshape(bs, slen, n_kv_heads * n_rep, head_dim)
    )

class GQAAttention(nn.Module):
    def __init__(self, embed_size, num_heads, n_kv_heads, max_seq_len):
        super(GQAAttention, self).__init__()
        self.num_heads = num_heads
        self.n_local_kv_heads = n_kv_heads
        self.head_dim = embed_size // num_heads
        
        assert (
            self.head_dim * num_heads == embed_size
        ), "Embedding size must be divisible by the number of heads"

        self.wq = nn.Linear(embed_size, embed_size)
        self.wk = nn.Linear(embed_size, self.n_local_kv_heads * self.head_dim)
        self.wv = nn.Linear(embed_size, self.n_local_kv_heads * self.head_dim)

        self.freqs_cis = precompute_freqs_cis(self.head_dim, max_seq_len)

    def forward(self, x):
        bsz, seqlen, _ = x.shape
        
        # Linear transformations to get Q, K, V
        xq = self.wq(x).view(bsz, seqlen, self.num_heads, self.head_dim)
        xk = self.wk(x).view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        xv = self.wv(x).view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        
        # Apply rotary position embedding to Q and K
        freqs_cis = self.freqs_cis[:seqlen]
        xq = apply_rotary_pos_emb(xq, freqs_cis)
        xk = apply_rotary_pos_emb(xk, freqs_cis)
        
        # Repeat K and V to match the number of Q heads
        xk = repeat_kv(xk, self.num_heads // self.n_local_kv_heads)
        xv = repeat_kv(xv, self.num_heads // self.n_local_kv_heads)
         
        # Attention computation
        scores = torch.matmul(xq, xk.transpose(-2, -1)) / math.sqrt(self.head_dim)
        scores = F.softmax(scores.float(), dim=-1)
        output = torch.matmul(scores, xv)
        
        # Reshape output
        output = output.view(bsz, seqlen, -1)  # (bsz, seqlen, embed_size)
        return output

if __name__ == '__main__':
    embed_size = 512
    num_heads = 8
    n_kv_heads = 2  # Less K/V heads than Q heads
    max_seq_len = 20
    seq_length = 10
    BN = 32

    x = torch.randn(BN, seq_length, embed_size)
    gqa = GQAAttention(embed_size, num_heads, n_kv_heads, max_seq_len)
    out = gqa(x)
    print(out.shape)