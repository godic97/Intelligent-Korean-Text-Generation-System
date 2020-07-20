import numpy as np
import util

data = util.loadData_preprocessing()
catalog = np.array([])
max = data.shape[0]
i = 0
for sample in data:
    for alpha in sample[0]:
        idx = np.where(catalog == alpha)
        if idx[0].size == 0:
            catalog = np.append(catalog, alpha)

    i += 1
    if i % 10000 == 0:
        print("max: ", max, " now: ", i)


print(catalog.shape)
id_2_dict = np.sort(catalog)
# np.save("../data/dict_store", id_2_dict)
print(id_2_dict)

id = 0
dict_2_id = {}
for dict in id_2_dict:
    dict_2_id[dict] = id
    id += 1

dict_2_id = np.array(dict_2_id)
print(dict_2_id)
# np.save("../data/id_store", dict_2_id)
