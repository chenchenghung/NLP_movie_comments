import os

data_path='/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/data'
target_path='/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/movie/target'

item=os.listdir(data_path)
print(len(item))
for i in range(len(item)):
    if i <27000:
        data= open(data_path+"/"+str(i)+'.txt','r')
        target= open(target_path+"/"+str(i)+'.txt','r')
        t=target.read()
        path=os.path.join('/Users/chenti-he/Desktop/movie/train',str(i)+'_'+str(t)+'.txt')
        with open(path,'wb') as f:
            f.write(data.read().encode())

        # print(data.read())
        # print(target.read())
    else:
        data= open(data_path+"/"+str(i)+'.txt','r')
        target= open(target_path+"/"+str(i)+'.txt','r')
        t=target.read()
        path=os.path.join('/Users/chenti-he/Desktop/movie/test',str(i)+'_'+str(t)+'.txt')
        with open(path,'wb') as f:
            f.write(data.read().encode())

    f.close()