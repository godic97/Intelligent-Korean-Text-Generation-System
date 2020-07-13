import pandas as pd
import util

dataSet = util.loadData()

for data in dataSet:
    # print("before: ", data)
    # pos = data[1].find(data[2])
    # print(pos)
    # if pos > -1:
    #     data[1] = data[1][0:pos]

    data[1] = util.removeBranchName(data[1], data[2])

    # print("after: ", data)

dataSet = pd.DataFrame(dataSet, columns={"상가업소": int, "상호명": "string", "지점명": "string",
                                                   "상권업종대분류코드": "string", "상권업종중분류코드": "string",
                                                   "상권업종소분류코드": "string", "표준산업분류코드": "string"})
# dataSet.to_csv("../data/store_non_branch_name.csv", na_rep="0", index=False, encoding="utf-8")