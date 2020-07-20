import numpy as np



data = np.load("../data/dict_industryCode.npy")
dict = np.load("../data/id_industryCode.npy",allow_pickle=True).item()
co_occurence = np.array([0 for i in range(data.size * data.size)]).reshape((data.size, data.size))
similaritySet = np.array([0 for i in range(data.size * data.size)]).reshape((data.size, data.size))

for x in data:
    x_idx = dict.get(x)
    for y in data:
        y_idx = dict.get(y)
        if x != y:
            if x[0] == y[0]:
                co_occurence[x_idx][y_idx] += 1
                co_occurence[y_idx][x_idx] += 1
                if x[:3] == y[:3]:
                    co_occurence[x_idx][y_idx] += 2
                    co_occurence[y_idx][x_idx] += 2

# np.save("../data/co_occurence_matrix_industryCode", co_occurence)
