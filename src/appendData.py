import pandas as pd
import util

data1 = pd.read_csv("../data/store_non_branch_name_attribute_1.csv", dtype={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})

print(data1)

data2 = pd.read_csv("../data/store_non_branch_name_attribute_2.csv", dtype={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
print(data2)

data3 = pd.read_csv("../data/store_non_branch_name_attribute_3.csv", dtype={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
print(data3)

data1 = data1.append(data2)
data1 = data1.append(data3)

# data1.to_csv("../data/store_non_branch_name_attribute_all.csv", na_rep="0", index=False, encoding="utf-8")

data = pd.read_csv("../data/store_non_branch_name_attribute_all.csv", dtype={"상호명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
print(data)