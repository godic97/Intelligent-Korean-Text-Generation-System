import numpy as np
import util
import pandas as pd

data = pd.read_csv("../data/remove_iname.csv", dtype={"상호명" : "string","상권업종소분류코드" : "string"}, na_filter=False)
data = np.array(data)
print(data[1807])
code2vec = util.loadIcode(val="vec")
char2id = util.loadChar(val="id")

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
# np.save("../data/corpus_remove_iname", corpus[:corpus.shape[0]-1])


# data = np.load("../data/corpus.npy", allow_pickle=True)
# i = 0
# for sample in data:
#     tmp = np.array([])
#     # print(sample[0])
#     j = 0
#     for alpha in sample[0]:
#         id = char2id.get(alpha, -1)
#
#         if id != -1:
#             tmp = np.append(tmp, id)
#             j = 0
#
#         elif j > 0:
#             if tmp[-1] == 1853:
#                 continue
#
#         else:
#             tmp = np.append(tmp, 1853)
#             j += 1
#
#
#     tmp = np.append(tmp, char2id["<end>"])
#     sample[0] = tmp
#     sample[1] = code2vec[sample[1]]
#     i = util.counter(i, data.shape[0])
#
# np.save("../data/corpus_tmp", data)


# data = np.load("../data/corpus.npy", allow_pickle=True)
# tmp = [0 for i in range(data.shape[0])]
# i = 0
#
# for d in data:
#     char = [f for f in d[0]]
#     code = [f for f in d[1]]
#     t = [char, code]
#     tmp[i] = t
#     i = util.counter(i, data.shape[0])

# tmp = to_categorical(tmp[:100, 0, 0])

# np.save("../data/tmp", tmp)

data = pd.read_csv("../data/first_word.csv", dtype="string")
data = np.array(data)

tmp = np.array([], dtype="int")

for alpha in data:
    id = char2id.get(alpha[0], -1)
    if id == -1:
        continue
    else:
        tmp = np.append(tmp, id)

tmp = np.sort(tmp)
print(tmp)
# np.save("../data/first_word", tmp)