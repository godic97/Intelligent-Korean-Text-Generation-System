import numpy as np
import util

data = util.loadData_preprocessing()
max = data.shape[0]
dict = np.array([])

i = 0
for sample in data:
    # 상호명, 상권업종대분류코드, 상권업종대분류명, 상권업종중분류코드, 상권업종중분류명, 상권업종소분류코드, 상권업종소분류명, 표준산업분류코드, 표준산업분류명
    if sample[5] != 0:
        idx = np.where(dict == sample[5])
        if idx[0].size == 0:
            dict = np.append(dict, sample[5])

    elif sample[3] != 0:
        idx = np.where(dict == sample[3])
        if idx[0].size == 0:
            dict = np.append(dict, sample[3])

    else:
        idx = np.where(dict == sample[1])
        if idx[0].size == 0:
            dict = np.append(dict, sample[1])

    i += 1
    if i % 10000 == 0:
        print("max: ", max, " now: ", i)

print(dict.shape)
dict = np.sort(dict)
# np.save("../data/dict_industryCode", dict)
print(dict)

id = 0
dict_2_id = {}
for code in dict:
    dict_2_id[code] = id
    id += 1

dict_2_id = np.array(dict_2_id)
print(dict_2_id)
# np.save("../data/id_industryCode", dict_2_id)