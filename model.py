

import torch.nn as nn
from config import ws, max_len
import torch.nn.functional as F
from dataset import get_dataloader
from torch.optim import Adam
import torch
import os
from tqdm import tqdm
import numpy as np

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.embedding = nn.Embedding(len(ws),100)
        self.fc= nn.Linear(max_len*100,2) #輸出為2分類
    def forward(self,input):
        #input:[batch_size, max_len]
        x=self.embedding(input) #embedding後變成 batch_size,max_len, 100]
        x=x.view([-1,max_len*100])
        # print(x.size())
        out=self.fc(x)
        # print(out)
        return F.log_softmax(out,dim=-1)



model=Model()
optimizer= Adam(model.parameters(),0.001)
if os.path.exists("./model/model.pkl"):
    model.load_state_dict(torch.load("./model/model.pkl"))
    optimizer.load_state_dict(torch.load("./model/optimizer.pkl"))
def train(epoch):
    for idx, (input,target) in enumerate(get_dataloader(train=True)):
        optimizer.zero_grad()
        output=model(input)
        loss=F.nll_loss(output,target)
        loss.backward()
        optimizer.step()
        print(epoch,idx,loss.item())

        if idx %100 ==0:
            torch.save(model.state_dict(),"./model/model.pkl")
            torch.save(optimizer.state_dict(),"./model/optimizer.pkl")

def eval():
    loss_list=[]
    acc_list=[]
    data_loader= get_dataloader(train=False)
    for idx, (input,target) in tqdm(enumerate(data_loader),total=len(data_loader),ascii=True,desc="測試集"):
        with torch.no_grad():
            output= model(input)
            cur_loss=F.nll_loss(output,target)
            loss_list.append(cur_loss.cpu().item())
            #計算準確率
            pred= output.max(dim=-1)[-1] #dim=-1, 以行找出最大值
            cur_acc= pred.eq(target).float().mean()
            acc_list.append(cur_acc.cpu().item())

    print("total_loss,acc:", np.mean(loss_list),np.mean(acc_list))

if __name__ == '__main__':
    # for i in range(1):
    #     train(i)
    eval()