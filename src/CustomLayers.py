import numpy as np
from tensorflow.keras.utils import to_categorical

def generator(corpus, batch_size, max_len):
    size = corpus.shape[0]

    while True:
        for i in range(size // batch_size):
            idx_end = [1853 for i in range(int(max_len[i]))]
            x_batch = np.array([idx_end for i in range(batch_size)])
            y_batch = np.array([idx_end for i in range(batch_size)])
            icode_batch = np.array(
                [[[0 for i in range(14)] for k in range(int(max_len[i]))] for j in range(batch_size)], dtype="float")

            for j in range(batch_size):
                now = i * batch_size + j
                x_batch[j][:corpus[now][0].shape[0] - 1] = corpus[now][0][:-1]
                y_batch[j][:corpus[now][0].shape[0] - 1] = corpus[now][0][1:]
                icode_batch[j] = corpus[now][1]*10

            x_batch = to_categorical(x_batch)
            y_batch = to_categorical(y_batch)

            yield [x_batch, icode_batch], y_batch