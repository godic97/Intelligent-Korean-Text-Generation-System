import numpy as np
import util

# data = util.loadData_preprocessing()
# data = data[:, [0, 5]]
# code2vec = util.loadIcode(val="vec")
# char2id = util.loadChar(val="id")

# corpus = ""
# i = 0
# for sample in data:
#     for alpha in sample[0]:
#         corpus += str(char2id[alpha]) + " "
#     corpus += str(char2id["<end>"]) + " "
#     i = util.counter(i, data.shape[0])
# # np.save("../data/test_corpus", corpus)
# corpus = np.array(corpus.split(" "))
# print(corpus.shape)
# print(corpus)
# np.save("../data/corpus", corpus[:corpus.shape[0]-1])

# i = 0
# for sample in data:
#     tmp = np.array([])
#     for alpha in sample[0]:
#         tmp = np.append(tmp, char2id[alpha])
#     tmp = np.append(tmp, char2id["<end>"])
#     sample[0] = tmp
#     sample[1] = code2vec[sample[1]]
#     i = util.counter(i, data.shape[0])

# np.save("../data/corpus", data)

from tensorflow.keras.utils import to_categorical
data = np.load("../data/corpus.npy", allow_pickle=True)
tmp = [0 for i in range(data.shape[0])]
i = 0

for d in data:
    char = [f for f in d[0]]
    code = [f for f in d[1]]
    t = [char, code]
    tmp[i] = t
    i = util.counter(i, data.shape[0])

# tmp = to_categorical(tmp[:100, 0, 0])

# np.save("../data/tmp", tmp)

print(tmp)

