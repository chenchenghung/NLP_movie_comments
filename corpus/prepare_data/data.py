from pymongo import MongoClient
import sys
import imp
imp.reload(sys)
import os

client= MongoClient(host="127.0.0.1",port=27017)
collection= client['douban']['dbmovie']




for num, item in enumerate(collection.find({},{'comment':1,'rating_by_writer':1})):
    data_path='/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/data'
    target_path='/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/target'
    if len(str(item['comment']))>0 and len(str(item['rating_by_writer']))>0:
        data_path= os.path.join(data_path,'{}'.format(num)+'.txt')
        target_path=os.path.join(target_path,'{}'.format(num)+'.txt')
        with open (data_path, 'wb') as f:
            if item['comment'] is None:
                f.write('0'.encode())
            else:
                f.write(item['comment'].encode())
        with open (target_path, 'wb') as f:
            # target=item['rating_by_writer'].decode('utf-8','strict')
            if item['rating_by_writer'] is None:
                f.write('0'.encode())
            else:
                f.write(str(item['rating_by_writer']).encode())
    f.close()