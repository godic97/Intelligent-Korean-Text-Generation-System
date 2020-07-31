import numpy as np
import util
import sys

char = util.loadChar(val="vec")
id_char = util.loadChar(val="dict")
icode = util.loadIcode(val="vec")
id_icode = util.loadIcode(val="dict")

char_similarity = np.array([0 for i in range(0, len(char) ** 2)]).reshape((len(char), len(char))).astype("float")
icode_similarity = np.array([0 for i in range(0, len(icode) ** 2)]).reshape((len(icode), len(icode))).astype("float")

char_top = np.array([0 for i in range(0,len(char))])
char_top_1 = np.array([0 for i in range(0,len(char))]).astype("float")
icode_top = np.array([0 for i in range(0,len(icode))])

max = len(char) ** 2
k = 0
for i in range(0, len(char)):
    top = -1
    for j in range(0, len(char)):
        char_similarity[i][j] = util.cos_similarity(char[id_char[i]], char[id_char[j]])
        if top < char_similarity[i][j] and i != j:
            top = char_similarity[i][j]
            char_top[i] = j
            char_top_1[i] = char_similarity[i][j]
        k = util.counter(k, max)

np.set_printoptions(threshold=sys.maxsize)

for i in range(0, len(char)):
    print("char: ", id_char[i], " top: ", id_char[char_top[i]])
    print("char: ", id_char[i], " top_1: ", char_top_1[i])


# for i in range(0, len(icode)):
#     top = 0
#     for j in range(0, len(icode)):
#         icode_similarity[i][j] = util.cos_similarity(icode[id_icode[i]], icode[id_icode[j]])
#         if top < icode_similarity[i][j] and i != j:
#             top = char_similarity[i][j]
#             icode_top[i] = j
#
# print(id_icode[icode_top])