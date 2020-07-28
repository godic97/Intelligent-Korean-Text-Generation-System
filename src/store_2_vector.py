import numpy as np
import pandas as pd
import sys
from sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize

import util

data = util.loadData_preprocessing()
data = data[:, [0, 5]]
num_data = data.shape[0]

corpus = util.loadCorpus(idx="id")
icode = util.loadIcode(idx="id")


count_vector = np.array([[0 for i in range(0, len(icode))] for i in range(0, len(corpus))])

cnt = 0
for store in data:
    for alpha in store[0]:
        count_vector[corpus[alpha]][icode[store[1]]] += 1
    cnt = util.counter(cnt=cnt, max=num_data)


print(count_vector)

# np.save("../data/count_vector", count_vector)

U, S, V = randomized_svd(count_vector, n_components=100, random_state=None)

# vector = normalize(U[:, :2])

vector = U[:, :2]

corpus2vec = {}

for c in icode:
    corpus2vec[c] = vector[icode[c]]

corpus2vec = np.array(corpus2vec)
np.save("../data/corpus2vec", corpus2vec)

np.set_printoptions(threshold=sys.maxsize)
print(corpus2vec)