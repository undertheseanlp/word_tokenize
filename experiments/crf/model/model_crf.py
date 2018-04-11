from os.path import join, dirname
import joblib
import sys
import pycrfsuite

from model.regex_tokenize import tokenize

sys.path.insert(0, dirname(__file__))
transformer = joblib.load(join(dirname(__file__), "transformer.bin"))
path = join(dirname(__file__), "model.bin")
estimator = pycrfsuite.Tagger()
estimator.open(path)


def predict(sentence):
    sentence = tokenize(sentence).split()
    tokens = [(token, "X") for token in sentence]
    x = transformer.transform([tokens])[0][0]
    tags = estimator.tag(x)
    return list(zip(sentence, tags))
