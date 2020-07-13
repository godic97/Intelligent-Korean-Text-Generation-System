import pandas as pd
import util


dataSet = util.loadData_pd("../data/store_non_branch_name_attribute.csv", dtype={"상호명" : "string",
                                                                     "상권업종대분류코드" : "string", "상권업종중분류코드" : "string",
                                                                     "상권업종소분류코드" : "string", "표준산업분류코드" : "string"})

dataSet1 = dataSet[:800000]
dataSet2 = dataSet[800001:1600000]
dataSet3 = dataSet[1600001:]

dataSet1 = pd.DataFrame(dataSet1, columns={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
dataSet2 = pd.DataFrame(dataSet2, columns={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
dataSet3 = pd.DataFrame(dataSet3, columns={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})

# dataSet1.to_csv("../data/store_non_branch_name_attribute_1.csv", na_rep="0", index=False, encoding="utf-8")
# dataSet2.to_csv("../data/store_non_branch_name_attribute_2.csv", na_rep="0", index=False, encoding="utf-8")
# dataSet3.to_csv("../data/store_non_branch_name_attribute_3.csv", na_rep="0", index=False, encoding="utf-8")

