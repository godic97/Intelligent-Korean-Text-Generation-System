import numpy as np
import util

import sys
np.set_printoptions(threshold=sys.maxsize)

fw = util.loadFirstWords()
code2vec = util.loadIcode(val="vec")
char2id = util.loadChar(val="id")
id2char = util.loadChar(val="dict")
char_size = id2char.shape[0]


from keras.models import load_model
from util import perplexity
model = load_model('../data/models/20200908_20_v3.h5', custom_objects={'perplexity':perplexity}, compile=False)
# model.summary()



def sentence_generation(model, length):
    ix = [fw[np.random.randint(fw.shape[0]-2)]]
    y_char = [id2char[ix[-1]]]

    X = np.zeros((1, length, char_size))
    Y = np.zeros((1, length, 14))

    Y[0] = np.array(code2vec['Q01A01']) * 10 #한식/백반/한정식

    for i in range(0, length):

        X[0][i][ix[-1]] = 1
        ix = util.weightedPick(model.predict([X[:, :i+1, :],Y[:, :i+1, :]])[0][-1])
        while ix == char_size - 1:
            ix = util.weightedPick(model.predict([X[:, :i + 1, :], Y[:, :i + 1, :]])[0][-1])

        y_char.append(id2char[ix[-1]])

        if ix == char_size - 2:
            break

    return ('').join(y_char)

for i in range(10):
    print(sentence_generation(model, 10))