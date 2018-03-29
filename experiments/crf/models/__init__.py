from os.path import join, dirname
import joblib
import sys
import time

import pycrfsuite
from to_columns import to_column

sys.path.insert(0, dirname(__file__))

transformer = joblib.load(join(dirname(__file__), "transformer.bin"))

model = join(dirname(__file__), "model.bin")
estimator = pycrfsuite.Tagger()
estimator.open(model)


def word_sent(sentence, format=None):
    if format == "text":
        sentence = to_column(sentence)
        X, y = transformer.transform([sentence])
        y = [estimator.tag(x) for x in X]
        tokenized_sentence = u""
        text = [i[0] for i in sentence]
        for tag, word in zip(y[0], text):
            if tag == "IW":
                tokenized_sentence = tokenized_sentence + u"_" + word
            else:
                tokenized_sentence = tokenized_sentence + word
            tokenized_sentence += " "
        format_sentence = ''
        path = join(dirname(dirname(__file__)), "punctuation.txt")
        with open(path, "r") as f:
            punctuations = f.read().split("\n")
        for word in tokenized_sentence.split("_"):
            if word not in punctuations:
                format_sentence += word[: -1] + "_"
        tokenized_sentence = format_sentence[:-1]
        return tokenized_sentence
    else:
        X, y = transformer.transform(sentence)
        start = time.time()
        y = [estimator.tag(x) for x in X]
        end = time.time()
        test_time = end - start
        print("test time: ", test_time)
        return y, test_time
