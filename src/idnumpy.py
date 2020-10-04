# -*- coding: utf-8 -*-


import numpy as np
import util

from tensorflow.keras.models import Model
from keras.models import load_model
corpus = util.loadCorpus(rm_iname=False)
code2vec = util.loadIcode(val="vec")

#store letters
char2id = util.loadChar(val="id")
id2char = util.loadChar(val="dict")

#store sectors
code2id = util.loadIcode(val="id")
id2code = util.loadIcode(val="dict")

model = load_model('../data/models/20200908_20_v3.h5', compile=False)

def getvec2id(input):
  result = ""
  for key, value in code2vec.items():
    for i in range(14):
      if(value[i] != input[i]):
        break
      if(i==13):
        result = code2id[key] 
  return result

print(code2id.get('Q01A01'))

print(len(id2char))
print(len(code2id))


charandId = np.zeros((len(id2char), len(code2id)))
len_corpus = corpus.shape[0]
cnt = 0

for i in range(len_corpus):
  cnt = util.counter(cnt, len_corpus)
  index_id = getvec2id(corpus[i][1])
  for j in range(corpus[i][0].shape[0]):
    index_char = (corpus[i][0][j]).astype(np.int32)
    charandId[index_char][index_id] +=1


np.save("../data/charandId",charandId)

charandId = np.load("../data/charandId.npy", allow_pickle=True)

index_middle_len = 0
index_big_len = 0

index_big = []
index_middle = []

current_index_middle = ''
current_index_big = ''
cnt = 0
for i in range(id2code.shape[0]):
  cnt = util.counter(cnt, id2code.shape[0])
  if current_index_big != id2code[i][0]:
    current_index_big = id2code[i][0]
    index_big.append(index_big_len)

  if current_index_middle != id2code[i][:3]:
    current_index_middle = id2code[i][:3]
    index_middle.append(index_middle_len)
  
  index_middle_len += 1
  index_big_len += 1

for i in range(len(index_big)):
  print(id2code[index_big[i]])

print(index_big)
print(id2code[607])

print(charandId.shape)
charandId = charandId
#가중치 1 2 3 
index_big_range  = 0
index_small_range = 0
weight = 0

cnt = 0
for i in range(charandId.shape[0]):
  cnt = util.counter(cnt, charandId.shape[0])
  for j in range(charandId.shape[1]):
    if charandId[i][j] != 0 :
      weight = charandId[i][j]
      for n in range(len(index_big)):
        if index_big[n] <= j :
          index_big_range = n
        if index_middle[n] <= j:
          index_middle_range = n
    
      if index_middle_range == len(index_middle)-1 :
        charandId[i][index_middle[index_middle_range]:758] += weight
      else :
        charandId[i][index_middle[index_middle_range]:758] += weight
      
      if index_middle_range == len(index_big)-1 :
        charandId[i][index_middle[index_big_range]:index_middle[index_big_range+1]] += weight
      else :
        charandId[i][index_middle[index_big_range]:index_middle[index_big_range+1]] += weight

print(charandId)

cnt = 0
for i in range(charandId.shape[0]):
  cnt = util.counter(cnt, charandId.shape[0])
  sum = charandId[i].sum()
  for j in range(charandId.shape[1]):
    if charandId[i][j] != 0:
      charandId[i][j] = charandId[i][j]/sum * 100

print(charandId)

np.save("../data/charandId_probability",charandId)
#charandId = np.load("/content/dirve/My Drive/Intelligent-Korean-Text-Generation-System/data/charAndId.npy", allow_pickle=True)