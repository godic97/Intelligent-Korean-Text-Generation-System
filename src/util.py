import pandas as pd
import numpy as np
import math


def loadData():
    # input: None
    # output: numpy.array:Store Data{int:store No., string:store name,
    #                             string:store branch name, string:industry classification code 1,
    #                             string:industry classification code 2, string:industry classification code 3}
    # load store.csv
    data = pd.read_csv("../data/store.csv", dtype={"상가업소": int, "상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종대분류명" : "string",
                           "상권업종중분류코드" : "string", "상권업종중분류명" : "string",
                           "상권업종소분류코드" : "string", "상권업종소분류명" : "string",
                           "표준산업분류코드" : "string", "표준산업분류명" : "string"})

    return np.array(data)

def loadData_pd(path, dtype):
    # input: path, data type
    # output: numpy.array:Store Data{int:store No., string:store name,
    #                             string:store branch name, string:industry classification code 1,
    #                             string:industry classification code 2, string:industry classification code 3}
    # load store.csv
    data = pd.read_csv(path, dtype=dtype)

    return np.array(data)

def loadData_preprocessing():
    # input: None
    # output: numpy.array:Store Data{int:store No., string:store name,
    #                             string:store branch name, string:industry classification code 1,
    #                             string:industry classification code 2, string:industry classification code 3}
    # load store.csv
    data = pd.read_csv("../data/store_non_branch_name_attribute_all.csv", dtype={"상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종대분류명" : "string",
                           "상권업종중분류코드" : "string", "상권업종중분류명" : "string",
                           "상권업종소분류코드" : "string", "상권업종소분류명" : "string",
                           "표준산업분류코드" : "string", "표준산업분류명" : "string"})

    return np.array(data)

def loadCorpus():
    data = np.load("../data/corpus_tmp.npy", allow_pickle=True)

    return data[:, 0], data[:, 1] #corpus, input

def removeBranchName(storeName, branchName):
    pos = storeName.find(branchName)
    if pos > -1:
        storeName = storeName[0:pos]

    return storeName

def loadId_2_dict():
    id_2_dict = np.load("../data/dict_2_id.npy")

    return id_2_dict

def cos_similarity(xp, yp):

    x_L2 = np.sum(xp ** 2)
    y_L2 = np.sum(yp ** 2)
    l2 = math.sqrt(x_L2) * math.sqrt(y_L2)

    similarity = np.dot(xp, yp)

    similarity = similarity / l2

    return similarity

def loadIcode(val="id"):
    if val =="dict":
        icode = np.load("../data/dict_industryCode.npy", allow_pickle=True)
    elif val == "id":
        icode = np.load("../data/id_industryCode.npy", allow_pickle=True).item()
    elif val =="vec":
        icode = np.load("../data/code2vec.npy", allow_pickle=True).item()
    return icode

def loadChar(val="id"):
    if val == "dict":
        char = np.load("../data/dict_char.npy", allow_pickle=True)
    elif val == "id":
        char = np.load("../data/id_char.npy", allow_pickle=True).item()
    elif val == "vec":
        char = np.load("../data/char2vec.npy", allow_pickle=True).item()
    return char

def counter(cnt=0, max=0):
    if cnt % 10000 == 0:
        print("max: ", max, " now: ", cnt)
    return cnt + 1

def weightedPick(weight):
    t = np.cumsum(weight)
    s = np.sum(weight)


    return np.searchsorted(t, np.random.rand(1) * s)

