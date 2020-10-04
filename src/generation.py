import numpy as np
import util

# import codecs
# sys.setrecursionlimit(10**7)
# 
# # stdout의 인코딩을 UTF-8로 강제 변환한다
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# 
# #python과 web 연동
# import cgi
# import cgitb
# cgitb.enable()
# print("content-type: text/html; charset=utf-8\n")
# data = cgi.FieldStorage()
# 
# #입력받은 변수
# exist_Keyword = False
# keyword = ''
# num_storeName = int(data.getvalue("num_storeName"))
# selectedId = data.getvalue("selectedId")
# doAddId = data.getvalue("doAddId")
# differ = int(data.getvalue("differ"))

# if data.getvalue("keyword") != keyword :
#     keyword = data.getvalue("keyword")
#     exist_Keyword = True
#
# #generation
# np.set_printoptions(threshold=sys.maxsize)
#
# fw = util.loadFirstWords()
# code2vec = util.loadIcode(val="vec")
# char2id = util.loadChar(val="id")
# id2char = util.loadChar(val="dict")
# char_size = id2char.shape[0]

differ = 50
selectedId = 'Q01A01'

fw = util.loadFirstWords()
code2vec = util.loadIcode(val="vec")
char2id = util.loadChar(val="id")
id2char = util.loadChar(val="dict")
dictionary = np.load("../data/dictionary.npy", allow_pickle=True)
char_size = id2char.shape[0]

from keras.models import load_model
from util import perplexity

model = load_model('../data/models/20200915_10_adam_v1.h5', custom_objects={'perplexity':perplexity}, compile=False)

model.summary()


def sentence_generation(model, length):
    first = np.random.randint(fw.shape[0]-2)
    ix = [fw[first]]
    y_char = [id2char[ix[-1]]]

    X = np.zeros((1, length, char_size))
    Y = np.zeros((1, length, 14))

    Y[0] = np.array(code2vec[selectedId]) * 10 #한식/백반/한정식

    for i in range(0, length):

        X[0][i][ix[-1]] = 1
        ix = util.weightedPick(model.predict([X[:, :i+1, :],Y[:, :i+1, :]])[0][-1], selectedId, differ)
        while ix == char_size - 1:
            ix = util.weightedPick(model.predict([X[:, :i + 1, :], Y[:, :i + 1, :]])[0][-1], selectedId, differ)

        y_char.append(id2char[ix[-1]])

        if ix == char_size - 2:
            break

    return ('').join(y_char), first


for i in range(10):
    store_name, first = sentence_generation(model, 20)
    while util.searchDict(store_name, dictionary, first) is True:
        store_name, first = sentence_generation(model, 20)
    print(store_name)
