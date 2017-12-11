# -*- coding: utf-8 -*
import gensim, logging

#  logging 用来输出训练日志
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

#  分好词的句子，每个句子已词列表的形式输入
sentences = [['first', 'sentence'], ['second','sentence']]

#  用以上句子练习词向量模型
model = gensim.models.Word2Vec(sentences, min_count=1)

#  输出单词sentence的词向量
print(model['sentence'])
