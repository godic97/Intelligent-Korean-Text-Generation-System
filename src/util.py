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

# def weightedPick(weight):
#     t = np.cumsum(weight)
#     s = np.sum(weight)
#
#     return np.searchsorted(t, np.random.rand(1) * s)

def loadIcAndChar():
    icAndChar = np.load("../data/charandId_probability.npy", allow_pickle=True)
    return icAndChar

def weightedPick(weight, char, differ):
    code2id = loadIcode(val="id")

    weight_len = weight.shape[0]
    weight_sum = 0
    delete_index = []
    icode_probability = loadIcAndChar()
    icode = code2id.get(char)

    # 업종 가중치 증가
    for i in range(icode_probability.shape[0]):
        weight = weight * (1 + icode_probability[i][icode] * 0.01)

    # 정규화
    normal_sum = weight.sum()
    weight /= normal_sum

    # 값이 낮은 가중치 삭제
    for i in range(weight_len):
        if (weight[i] < 0.001):
            delete_index.append(i)
            weight_sum += weight[i]
            weight[i] = 0.
    for i in range(weight_len):
        if not i in delete_index:
            weight[i] += weight_sum / len(delete_index)

    # 오름차순으로 나열
    sortedWeight = np.sort(weight)
    sortedIndex = np.argsort(weight)

    # 범위함수로 변환
    t = np.cumsum(sortedWeight)
    s = np.sum(sortedWeight)

    # np.random.normal(정규분포 평균, 표준편차, (행, 열) or 개수) : 정규 분포 확률 밀도에서 표본 추출
    # mean 평균/std 표준편차 (기준 0.3)
    std_array = [0.3, 0.275, 0.225, 0.2, 0.175, 0.15, 0.1, 0.075, 0.05]
    mean = 1
    std = std_array[int(differ / 10) - 1]
    data = 0;

    while (1):
        data = np.random.normal(mean, std, 1)
        if data > 1:
            data -= 2
        if data > 0.5:
            break;
            print(data)

    # 범위 선택으로 인해 인덱스 넘어가는 것을 방지
    selectedIndex = np.searchsorted(t, data * s)
    if selectedIndex == sortedIndex.shape:
        selectedIndex = sortedIndex.shape - 1

    result = sortedIndex[selectedIndex]

    return result

def loadCorpus(rm_iname=False):
    if rm_iname == True:
        corpus = np.load("../data/corpus_remove_iname.npy", allow_pickle=True)
    elif rm_iname == False:
        corpus = np.load("../data/corpus.npy", allow_pickle=True)

    return corpus


from keras import backend as K
def perplexity(y_true, y_pred):
    x_entropy = K.categorical_crossentropy(y_true, y_pred)
    hx = K.exp(x_entropy)

    return hx

def loadFirstWords():
    data = np.load("../data/first_word.npy")
    return data

def searchIdx(id):
    idx = np.load("../data/startIndex.npy")

    return idx[id]

def searchDict(name, dictionary, first):
    char2id = loadChar(val="id")
    idx = searchIdx(first)

    while char2id[name[0]] == dictionary[idx][0]:
        isSame = True
        for i, id in enumerate(name):
            if id == "<":
                break
            if char2id[id] != dictionary[idx][i]:
                isSame = False
                break
        if isSame is True:
            return True
        idx += 1

    return False


