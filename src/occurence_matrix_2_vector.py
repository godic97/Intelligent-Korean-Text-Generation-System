from sklearn.utils.extmath import randomized_svd
from sklearn.preprocessing import normalize
import numpy as np
import util

occurence = np.load("../data/occurence_matrix_industryCode.npy")
dict = np.load("../data/id_industryCode.npy", allow_pickle=True).item()
U, S, V = randomized_svd(occurence, n_components=100, random_state=None)
# U, S, V = np.linalg.svd(occurence)

vector = U[:, :14]

a = vector[dict["D14A14"]]
b = vector[dict["D14A13"]]
# print("D14A14: ", a)
# print("D14A13: ", b)
print("D14A14 & D14A13: ", util.cos_similarity(a, b))

b = vector[dict["D05A06"]]
# print("D14A14: ", a)
# print("D05A06: ", b)
print("D14A14 & D05A06: ", util.cos_similarity(a, b))

b = vector[dict["F05A01"]]
# print("D14A14: ", a)
# print("F05A01: ", b)
print("D14A14 & F05A01: ", util.cos_similarity(a, b))

a = vector[dict["R13A03"]]
b = vector[dict["S01B01"]]
# print("R13A03: ", a)
# print("S01B01: ", b)
print("R13A03 & S01B01: ", util.cos_similarity(a, b))

vector_industryCode = {}
for code in dict:
    vector_industryCode[code] = vector[dict[code]]

vector_industryCode = np.array(vector_industryCode)
np.save("../data/code2vec", vector_industryCode)
# print(vector_industryCode)