import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def precompute_sincos_pos_emb(dim, max_seq_len):
    """预计算正弦-余弦位置编码"""
    position = torch.arange(0, max_seq_len).unsqueeze(1).float()
    div_term = torch.exp(torch.arange(0, dim, 2).float() * -(math.log(10000.0) / dim))
    pos_emb = torch.zeros(max_seq_len, dim)
    pos_emb[:, 0::2] = torch.sin(position * div_term)
    pos_emb[:, 1::2] = torch.cos(position * div_term)
    return pos_emb  # Shape: (max_seq_len, dim)

def repeat_kv(x: torch.Tensor, n_rep: int) -> torch.Tensor:
    """重复K和V头以匹配Q头的数量"""
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

        self.pos_emb = precompute_sincos_pos_emb(embed_size, max_seq_len)

    def forward(self, x):
        bsz, seqlen, _ = x.shape
        
        # 获取正弦-余弦位置编码
        pos_emb = self.pos_emb[:seqlen, :].unsqueeze(0).to(x.device)
        
        # Linear transformations to get Q, K, V
        xq = self.wq(x).view(bsz, seqlen, self.num_heads, self.head_dim)
        xk = self.wk(x).view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        xv = self.wv(x).view(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        
        # Apply sinusoidal position embedding to Q and K
        pos_emb = pos_emb.view(1, seqlen, 1, self.head_dim)  # 调整位置编码形状
        xq = xq + pos_emb.expand(bsz, seqlen, self.num_heads, self.head_dim)
        xk = xk + pos_emb.expand(bsz, seqlen, self.n_local_kv_heads, self.head_dim)
        
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

# 参数设定
embed_size = 16    # 嵌入维度
num_heads = 4      # 注意力头的数量
n_kv_heads = 2     # K和V的头的数量
max_seq_len = 10   # 序列的最大长度
batch_size = 2     # 批大小

# 创建一个随机输入张量 (batch_size, seq_len, embed_size)
x = torch.randn(batch_size, max_seq_len, embed_size)

# 实例化注意力模型
attention = GQAAttention(embed_size, num_heads, n_kv_heads, max_seq_len)

# 执行前向传播
output = attention(x)

# 输出形状 (batch_size, seq_len, embed_size)
print("Output shape:", output.shape)