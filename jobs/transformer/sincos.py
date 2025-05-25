import torch
import torch.nn as nn
# class PositionEncoding(nn.Module):
#     def __init__(self,num_hiddens,dropout,max_len=1000):
#         super(PositionEncoding,self).__init__()
#         self.dropout=nn.Dropout(dropout)
#         self.P=torch.zeros((1,max_len,num_hiddens))
#         X=torch.arange(max_len).reshape(-1,1)/torch.pow(10000,torch.arange(0,num_hiddens,2)/num_hiddens)
#         #切片操作：start:stop:step(初始值：结束值：步长)
#         self.P[:,:,0::2]=torch.sin(X)
#         self.P[:,:,1::2]=torch.cos(X)
#     def forward(self,X):
#         X=X+self.P[:,:X.shape[1],:]
#         return self.dropout(X)

class Sincospositionenciding(nn.Module):
    def __init__(self,embed_size,max_len=1000,dropout=0.1):
        super(Sincospositionenciding,self).__init__()
        self.embed_size=embed_size
        self.max_len=max_len
        self.dropout=nn.Dropout(dropout)
        self.P=torch.zeros((1,max_len,embed_size))
        X=torch.arange(max_len).reshape(-1,1)/torch.pow(10000,torch.arange(0,embed_size,2)/embed_size)
        self.P[:,:,0::2]=torch.sin(X)
        self.P[:,:,1::2]=torch.cos(X)
    def forward(self,X):
        X=X+self.P[:,:X.shape[1],:]
        X=self.dropout(X)
        return X 
embed_size=512
BN=10
X=torch.randn((BN,100,embed_size))
position_encoding=Sincospositionenciding(embed_size)
out=position_encoding(X)
print(out.shape)
    

class Position(nn.Module):
    def __init__(self,embed_size,max_len=1000,dropout=0.2):
        super(Position,self).__init__()
        self.embed_size=embed_size
        self.max_len=max_len
        self.P=torch.zeros((1,max_len,embed_size))
        self.dropout=nn.Dropout(dropout)
        X=torch.arange(max_len).reshape(-1,1)/torch.pow(1000,torch.arange(0,embed_size,2)/embed_size)
        self.P[:,:,0::2]=torch.sin(X)
        self.P[:,:,1::2]=torch.cos(X)
    def forward(self,X):
        X=X+self.P[:,:X.shape[1],:]
        return self.dropout(X)


BN=10
seq_len=100
embed_size=512
X=torch.randn((BN,seq_len,embed_size))
pos=Position(embed_size)
out=pos(X)
print(X.shape)

# # 假设嵌入维度为 8，dropout 率为 0.1，最大序列长度为 20
# position_encoding = PositionEncoding(num_hiddens=8, dropout=0.1, max_len=20)

# # 假设输入张量的维度为 (2, 10, 8)，即 batch_size=2, seq_length=10, embedding_dim=8
# X = torch.zeros((2, 10, 8))

# # 经过位置编码后的输出
# output = position_encoding(X)
# print(output.shape)
