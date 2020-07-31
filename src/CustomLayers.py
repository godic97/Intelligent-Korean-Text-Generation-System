import numpy as np
from tensorflow.keras.utils import to_categorical

def generator(corpus, batch_size):
    size = corpus.shape[0]

    while True:
        idx = np.random.permutation(size)
        X_char_data = corpus[idx, 0]
        X_icode_data = corpus[idx, 1]
        y_data = corpus[idx, 0]

        for i in range(size // batch_size):
            x_batch = X_char_data[i * batch_size: (i+1)*batch_size]
            y_batch = y_data[i * batch_size: (i+1)*batch_size]

            yield to_categorical(x_batch).reshape((int(batch_size / 100), 100, 2276)), to_categorical(y_batch).reshape((int(batch_size / 100), 100, 2276))