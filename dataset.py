from torch.utils.data import DataLoader, Dataset
import os
from lib.cut_sentence import cut
from config import max_len, ws
import re
import torch

def tokenlize(content):
    content=re.sub("<.*?>"," ", content)
    filters= ['/t','/n','/x97','/x96','$','#','&','$','\"','\'','/.']
    content= re.sub("|".join(filters)," ",content)
    tokens= [i.strip().lower() for i in content.split()]
    return tokens

class ImdbDataset(Dataset):
    def __init__(self,train=True):
        self.train_data_path=r'/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/train'
        self.test_data_path=r'/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/test'
        data_path=self.train_data_path if train else self.test_data_path

        #所有文件的路徑
        self.total_file_path=[]
        for path_name in os.listdir(data_path):
            path_list= os.path.join(data_path,path_name)
            self.total_file_path.append(path_list)

    def __getitem__(self, index):
        file_path=self.total_file_path[index]
        label_str= file_path.split('/')[-1].split('_')[1][:1]
        label= 0 if int(label_str)<3 else 1
        tokens= cut(open(file_path).read())

        return tokens,label

    def __len__(self):
        return len(self.total_file_path)

def collate_fn(batch):
    #get item 回傳的([tokens,label],[tokens,label]) 把token,label分開
    content, label=list(zip(*batch))
    content=[ws.transform(i,max_len=max_len) for i in content]
    content=torch.LongTensor(content)
    label= torch.LongTensor(label)
    return content, label

def get_dataloader(train=True):
    imdb_dataset=ImdbDataset(train)
    data_loader=DataLoader(imdb_dataset, batch_size=128, shuffle=True,collate_fn=collate_fn)
    return data_loader
if __name__ == '__main__':

    db=ImdbDataset()
    # print(db.__getitem__(1))
    # print(len(ws))
    for idx,(input,targets) in enumerate(get_dataloader()):
        print(idx)
        print(input.size())
        print(targets.size())
        break