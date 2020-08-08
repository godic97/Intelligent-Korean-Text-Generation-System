import numpy as np
from tensorflow.keras.utils import to_categorical

def generator(x_data, y_data, batch_size):
    size = x_data.shape[0]

    while True:
        for i in range(size // batch_size):
            x_batch = to_categorical(x_data[i * batch_size: (i + 1) * batch_size])
            y_batch = to_categorical(y_data[i * batch_size: (i + 1) * batch_size])

            yield x_batch, y_batch