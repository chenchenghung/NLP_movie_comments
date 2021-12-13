#獲取停用詞
import config

stopwords=[i.strip() for i in open(config.stopwords_path).readlines()]