import numpy as np

import util

data = util.loadData_preprocessing()
catalog = np.array([], )
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
catalog = np.sort(catalog)
np.save("../data/catalog", catalog)
print(catalog)