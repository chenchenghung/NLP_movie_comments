import pickle

stopwords_path='/Users/chenti-he/PycharmProjects/NLP_movie_comments/corpus/user_dict/stopwords.txt'

max_len=20  # seq_len, 句長 hidden layer

ws=pickle.load(open("./model/ws.pkl","rb"))