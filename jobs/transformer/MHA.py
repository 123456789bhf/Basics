import torch
import torch.nn as nn

# class Multiheadattention(nn.Module):
#     def __init__(self,num_head,embed_size):
#         super(Multiheadattention,self).__init__()
#         self.num_head=num_head
#         self.head_size=embed_size//num_head
#         self.embed_size=embed_size
#         assert (
#             self.head_size*num_head==embed_size
#         ),"error"
#         self.querys=nn.Linear(embed_size,embed_size)
#         self.keys=nn.Linear(embed_size,embed_size)
#         self.values=nn.Linear(embed_size,embed_size)
#         self.FN=nn.Linear(embed_size,embed_size)
#     def forward(self,query,key,value,masked=None):
#         BN=query.size(0)
#         seq_length=query.size(1)
#         querys=self.querys(query)
#         keys=self.keys(key)
#         values=self.values(value)
        
#         q=querys.view(BN,seq_length,self.head_size,self.num_head).transpose(1,2)
#         k=keys.view(BN,seq_length,self.head_size,self.num_head).transpose(1,2) 
#         v=values.view(BN,seq_length,self.head_size,self.num_head).transpose(1,2)
#         energy=torch.matmul(q,k.transpose(-2,-1))/(self.head_size**0.5)
#         if masked is not None:
#             energy.masked_fill(masked==0,float('1e-20'))
#         attention=torch.softmax(energy,dim=-1)
#         out=torch.matmul(attention,v)
#         out=out.transpose(1,2).contiguous().view(BN,seq_length,self.embed_size)
#         out=self.FN(out)
#         return out



        

# class Multiheadattention(nn.Module):
#     def __init__(self,num_head,embed_size):
#         super(Multiheadattention,self).__init__()
#         self.num_head=num_head
#         self.head_size=embed_size//num_head
#         self.embed_size=embed_size
#         assert (
#             self.num_head*self.head_size==self.embed_size
#         ),'error'
#         self.query=nn.Linear(embed_size,embed_size)
#         self.key=nn.Linear(embed_size,embed_size)
#         self.value=nn.Linear(embed_size,embed_size)
#         self.Fn=nn.Linear(embed_size,embed_size)
#     def forward(self,querys,keys,values,mask=None):
#         BN,seq_length,_=querys.size()
#         query=self.query(querys)
#         key=self.key(keys)
#         value=self.value(values)
#         q=query.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
#         k=key.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
#         v=value.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
#         enery=torch.matmul(q,k.transpose(-2,-1))/(self.head_size**0.5)
#         if mask is not None:
#             energy.masked_fill(mask==0,float('-1e20'))
#         attention=torch.softmax(enery,dim=-1)
#         out=torch.matmul(attention,v)
#         out=out.transpose(1,2).contiguous().view(BN,seq_length,self.embed_size)
#         out=self.Fn(out)
#         return out

class Multiheadattention(nn.Module):
    def __init__(self,embed_size,num_head):
        super(Multiheadattention,self).__init__()
        self.embed_size=embed_size
        self.head_size=embed_size//num_head
        self.num_head=num_head
        
        assert (
            self.num_head*self.head_size==self.embed_size
        ),'error'
        self.query=nn.Linear(embed_size,embed_size)
        self.key=nn.Linear(embed_size,embed_size)
        self.value=nn.Linear(embed_size,embed_size)
        self.fn=nn.Linear(embed_size,embed_size)
    def forward(self,querys,keys,values,mask=None):
        BN=querys.size(0)
        seq_length=querys.size(1)
        querys=self.query(querys)
        keys=self.key(keys)
        values=self.value(values)
        q=querys.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
        k=keys.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
        v=values.view(BN,seq_length,self.num_head,self.head_size).transpose(1,2)
        energy=torch.matmul(q,k.transpose(-2,-1))/(self.head_size**0.05)
        if mask is not None:
            energy.masked_fill(mask==0,float('-1e20'))
        attention=torch.softmax(energy,dim=-1)
        out=torch.matmul(attention,v)
        out=out.transpose(1,2).contiguous().view(BN,seq_length,self.embed_size)
        out=self.fn(out)
        return out




if __name__=='__main__':
    embed_size=512
    num_head=8
    seq_length=10
    BN=32
    x=torch.randn(BN,seq_length,embed_size)
    MHA=Multiheadattention(embed_size,num_head)
    out=MHA(x,x,x)
    print(out.shape)