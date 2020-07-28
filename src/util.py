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

def loadIcode(idx="id"):
    if idx =="dict":
        icode = np.load("../data/dict_industryCode.npy", allow_pickle=True)
    elif idx == "id":
        icode = np.load("../data/id_industryCode.npy", allow_pickle=True).item()
    return icode

def loadCorpus(idx="id"):
    if idx == "dict":
        corpus = np.load("../data/dict_store.npy", allow_pickle=True)
    elif idx == "id":
        corpus = np.load("../data/id_store.npy", allow_pickle=True).item()
    return corpus

def counter(cnt=0, max=0):
    if cnt % 10000 == 0:
        print("max: ", max, " now: ", cnt)
    return cnt + 1