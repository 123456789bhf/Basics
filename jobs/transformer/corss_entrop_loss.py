import torch 



def cross_entropy_loss(pre_label,true_label):
    return -torch.log(pre_label[range(len(pre_label)),true_label])
pre_label=torch.tensor([[0.1,0.2,0.7],[0.3,0.4,0.3]])
true_label=torch.tensor([0,2])
print(cross_entropy_loss(pre_label,true_label))


