import util
import numpy as np
from sklearn.preprocessing import normalize
# import sys
# np.set_printoptions(threshold=sys.maxsize)

corpus = util.loadCorpus()
id2char = util.loadChar(val="dict")
char2id = util.loadChar(val="id")
code2vec = util.loadIcode(val="vec")

# i = 0
# for sample in corpus:
#     for id in sample[0]:
#         if (2263<=id<=2274) or (0<= id <15) or (24< id <= 420):
#             id = 1853
#     i = util.counter(i, corpus.shape[0])
# print(corpus)
# 2263~2274, 0~420(15~24는 숫자라서 제외, 띄어쓰기 는 0)
# np.save("../data/dict_char.npy", new_id2char)

for vec in code2vec:
    code2vec[vec] = normalize(code2vec[vec].reshape((1,14))).reshape((14))
    print(code2vec[vec])
print(code2vec)
np.save("../data/code2vec", code2vec)

# new_char2id = {}
# i = 0
# for char in id2char:
#     print(char)
#     new_char2id[char] = i
#     i+=1
#
# new_char2id = np.array(new_char2id)
# print(new_char2id)
# np.save("../data/id_char", new_char2id)