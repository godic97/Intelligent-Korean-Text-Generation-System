import pandas as pd
import numpy as np



def loadData():
    # input: None
    # output: numpy.array:Store Data{int:store No., string:store name,
    #                             string:store branch name, string:industry classification code 1,
    #                             string:industry classification code 2, string:industry classification code 3}
    # load store.csv
    data = pd.read_csv("../data/store.csv", dtype={"상가업소": int, "상호명": "string", "지점명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})

    return np.array(data)

def loadData_pd(path, dtype):
    # input: None
    # output: numpy.array:Store Data{int:store No., string:store name,
    #                             string:store branch name, string:industry classification code 1,
    #                             string:industry classification code 2, string:industry classification code 3}
    # load store.csv
    data = pd.read_csv(path, dtype=dtype)

    return np.array(data)

def removeBranchName(storeName, branchName):
    pos = storeName.find(branchName)
    if pos > -1:
        storeName = storeName[0:pos]

    return storeName
