#分詞
import jieba
import config
import jieba.posseg as psg
import string
from lib import stopwords
import logging

#關閉jieba日誌
jieba.setLogLevel(logging.INFO)

# jieba.load_userdict(config.user_dict_path)
#準備英文字符
letters=string.ascii_lowercase+'+'


def cut_sentence_by_word(sentence):
    #實現中英文分詞
    #python和c++哪個難?  --> [python, 和, c++, 哪, 個, 難,?]
    #依照 單個字劃分進行
    temp=''
    result=[]
    for word in sentence:
        #把英文單詞進行拼接
        if word.lower() in letters:
            temp+= word
        else:
            if temp != '': #出現了中文 把英文添加到結果中
                result.append(temp.lower())
                temp=''
            result.append(word.strip())#當前的中文字
    if temp !='': #最後出現英文要捕捉
        result.append(temp.lower())
    return result

def cut(sentence,by_word=False, use_stopword=False,with_sg=False):
    #是否單字分詞 停用詞 返回詞性?

    if by_word:
        result=cut_sentence_by_word(sentence)
    #不是按照單個字進行劃分
    else:
        result=psg.lcut(sentence)
        result=[(i.word,i.flag) for i in result]
        if not with_sg:
            result=[i[0] for i in result]
    #是否使用停用詞
    if use_stopword:
        result= [i for i in result if i not in stopwords ]
    return result

