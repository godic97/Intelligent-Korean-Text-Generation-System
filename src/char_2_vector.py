import numpy as np
import pandas as pd
import sys
from sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize

import util

data = util.loadData_preprocessing()
data = data[:, [0, 5]]
num_data = data.shape[0]

char = util.loadChar(val="id")
icode = util.loadIcode(val="id")

count_vector = np.array([[0 for i in range(0, len(icode))] for i in range(0, len(char))])

cnt = 0
for store in data:
    for alpha in store[0]:
        count_vector[char[alpha]][icode[store[1]]] += 1
    cnt = util.counter(cnt=cnt, max=num_data)


print(count_vector)

# np.save("../data/count_vector", count_vector)

U, S, V = randomized_svd(count_vector, n_components=100, random_state=None)

# vector = normalize(U[:, :2])

vector = U

char2vec = {}

for c in char:
    char2vec[c] = vector[char[c]]

char2vec = np.array(char2vec)
# np.save("../data/char2vec", char2vec)

np.set_printoptions(threshold=sys.maxsize)
print(char2vec)
