from tensorflow.keras.utils import to_categorical
import numpy as np
import util
from CustomLayers import generator

# corpus, input = util.loadCorpus()
corpus = np.load("../data/corpus.npy", allow_pickle=True)
code2vec = util.loadIcode(val="vec")
char2id = util.loadChar(val="id")
id2char = util.loadChar(val="dict")

# train_X = corpus[: corpus.shape[0]-1]
# train_Y = corpus[1: corpus.shape[0]]

batch_size = 30000

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, TimeDistributed


model = Sequential()
model.add(LSTM(256, input_shape=(None, 2276), return_sequences=True))
model.add(LSTM(256, return_sequences=True))
model.add(TimeDistributed(Dense(2276, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(generator(corpus, batch_size), epochs=10, steps_per_epoch=train_X.shape[0]//batch_size, verbose=1)

# from keras.models import load_model
# model = load_model('timestep_N.h5')

model.save('timestep_N.h5')

def sentence_generation(model, length):
    ix = [np.random.randint(2276)]
    y_char = [id2char[ix[-1]]]
    print(ix[-1], '번 글자', y_char[-1], '로 예측을 시작!')

    # X = np.zeros((1, 2, 2276))  # (1, 2, 2276) 크기의 X 생성. 즉, LSTM의 입력 시퀀스 생성
    X = np.zeros((1, length, 2276))

    for i in range(0, length):
        # X[0][0] = X[0][1]
        # X[0][1][ix[-1]] = 1
        X[0][i][ix[-1]] = 1

        # ix = util.weightedPick(model.predict(X)[0][-1])
        ix = util.weightedPick(model.predict(X[:, :i+1, :])[0][-1])
        y_char.append(id2char[ix[-1]])

    return ('').join(y_char)


# model.save('timestep_N.h5')

print(sentence_generation(model, 100))