import pandas as pd
import numpy as np
import util

dataSet = util.loadData_pd("../data/store_non_branch_name.csv", dtype={"상가업소" : int, "상호명" : "string", "지점명" : "string",
                                                                     "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                                                                     "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})
print(dataSet)
dataSet = dataSet[:, [1, 3, 4, 5, 6]]
print(dataSet)
dataSet = pd.DataFrame(dataSet, columns={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
dataSet.to_csv("../data/store_non_branch_name_attribute.csv", na_rep="0", index=False, encoding="utf-8")