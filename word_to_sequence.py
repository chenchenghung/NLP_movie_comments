

#構建辭典
#計算詞頻

class Word2Sequence:

    UNK_TAG='UNK'
    PAD_TAG='PAD'

    UNK=0
    PAD=1

    def __init__(self):
        self.dict={
            self.UNK_TAG:self.UNK,
            self.PAD_TAG:self.PAD
        }
        self.count={}

    #計算詞頻，把句子餵入字典前先統計
    def fit(self,sentence):
        for word in sentence:
            self.count[word]=self.count.get(word,0)+1

    def build_vocab(self,min=5,max=None,max_features=None):
        if min is not None:
            self.count={word:value for word,value in self.count.items() if value >min}

        if max is not None:
            self.count={word:value for word,value in self.count.items() if value <max}

        if max_features is not None:
            temp=sorted(self.count.items(), key=lambda x:x[-1],reverse=True)[:max_features]
            self.count=dict(temp)

        for word in self.count:
            self.dict[word]=len(self.dict)

        #反轉辭典
        self.inverse_dict=dict(zip(self.dict.values(),self.dict.keys()))


    def transform(self,sentence,max_len=None):
        #將句子轉成序列
        if max_len is not None:
            if max_len> len(sentence):
                sentence= sentence+ [self.PAD_TAG]*(max_len-len(sentence))
            if max_len< len(sentence):
                sentence= sentence[:max_len]

        return [self.dict.get(word,self.UNK) for word in sentence]


    def inverse_transform(self,indices):
        #將序列轉回句子

        return [self.inverse_dict.get(idx) for idx in indices]


    def __len__(self):
        return len(self.dict)
if __name__ == '__main__':
    ws= Word2Sequence()
    ws.fit(['我','今天','出門','去','寄','包裹'])
    ws.fit(['我','今天','不','想','出門'])
    ws.build_vocab(min=0)
    ret=ws.transform(['我','看','不','到'],max_len=15)
    print(ws.count)
    print(ws.dict)
    print(ret)
    print(ws.inverse_transform(ret))
    print(len(ws))