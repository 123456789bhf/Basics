import torch

def rotate_half(x):
    """Splits the last dimension into two and performs a rotation (cosine, sine)."""
    x1, x2 = x.chunk(2, dim=-1)
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(x, freqs):
    """Applies the rotary position embedding."""
    return (x * freqs.cos()) + (rotate_half(x) * freqs.sin())

# Precompute frequencies for rotary embeddings
def precompute_freqs_cis(dim, max_seq_len):
    """Compute the rotary position encodings."""
    inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
    pos_seq = torch.arange(0, max_seq_len).float()
    freqs = torch.einsum("i,j->ij", pos_seq, inv_freq)
    return torch.cat((freqs, freqs), dim=-1)

# Example usage
seq_len = 10
embed_dim = 64

# Create a dummy tensor of embeddings
x = torch.randn(32, seq_len, embed_dim)

# Precompute rotary position encodings
freqs_cis = precompute_freqs_cis(embed_dim, seq_len)

# Apply rotary position embeddings to the input embeddings
x_rotary = apply_rotary_pos_emb(x, freqs_cis[:seq_len])

print(x_rotary.shape)  # Should be the same as x