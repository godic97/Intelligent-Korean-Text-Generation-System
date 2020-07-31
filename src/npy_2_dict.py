# from six.moves import cPickle as pickle
import numpy as np
import json
import util


id = util.loadChar(val="vec")
val = util.loadChar(val="id")
save = {}
for d in val:
    save[d] = id[d]

f = open("../data/code2vec.json", 'w')
json.dump(save,f)