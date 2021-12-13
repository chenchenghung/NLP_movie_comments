if __name__ == '__main__':
    from word_to_sequence import Word2Sequence
    import pickle
    import os
    from lib.cut_sentence import cut
    from tqdm import tqdm

#使用word_sequence製作字典

    ws=Word2Sequence()
    data_path=r'/Users/chenti-he/Desktop/movie/train'

    file_names= os.listdir(data_path)
    file_paths= [os.path.join(data_path,file_name) for file_name in os.listdir(data_path) ]
    for file_path in tqdm(file_paths):
        sentence= cut(open(file_path).read(),by_word=True)
        ws.fit(sentence)
    ws.build_vocab(min=5,max_features=10000)
    pickle.dump(ws,open("./model/ws.pkl","wb"))
    # print(ws.dict)
    print(len(ws))


