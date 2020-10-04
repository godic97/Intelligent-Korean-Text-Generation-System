import numpy as np
import util

si = np.load("../data/startIndex.npy")
dictionary = np.load("../data/dictionary.npy", allow_pickle=True)
id2char = util.loadChar(val="dict")
fw = np.load("../data/first_word.npy")
# fw = np.array([], dtype="int")

# for idx in si:
#     print(id2char[int(dictionary[idx][0])])

# for i in range(si.shape[0]-1):
#     print(int(dictionary[si[i]][0]), " ", fw[i])

# for idx in range(si.shape[0]-1):
#     fw = np.append(fw, int(dictionary[si[idx]][0]))
#     print(int(dictionary[si[idx]][0]))
#
# np.save("../data/first_word", fw)

dictIcode = util.loadIcode(val="dict")
code2vec = util.loadIcode(val="vec")

for key in code2vec:
    print("key: ", key, " vec: ", code2vec[key])
