import pandas as pd
import numpy as np
import util

data1 = pd.read_csv("../data/store_01.csv",
                    dtype={"상가업소" : int, "상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                           "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})
print(np.array(data1)[0])

data2 = pd.read_csv("../data/store_02.csv", dtype={"상가업소" : int, "상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                           "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})
print(data2)

data3 = pd.read_csv("../data/store_03.csv", dtype={"상가업소" : int, "상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                           "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})
print(data3)

data4 = pd.read_csv("../data/store_04.csv", dtype={"상가업소" : int, "상호명" : "string", "지점명" : "string",
                           "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                           "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})
print(data4)


# data1 = data1.append(data2)
# data1 = data1.append(data3)
# data1 = data1.append(data4)
#
# print(data1)
#
# data1.to_csv("../data/store.csv", na_rep="0", index=False, encoding="utf-8")


data = util.loadData()
print(data)

