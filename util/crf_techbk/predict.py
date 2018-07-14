# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sklearn_crfsuite
from process import sent2features
from text import sylabelize


CRF = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True,
    model_filename='models/model.bin'
)


def tokenize(text, format=None):
    # if isinstance(text, str):
    #     text = text.decode('utf-8')
    text = sylabelize(text)

    X = [sent2features(text)]
    y_pred = CRF.predict(X)
    words = []
    word = ""
    for x, y in zip(text, y_pred[0]):
        # max_key = max(y_m.iteritems(), key=operator.itemgetter(1))[0]
        # print x, y
        if y == 'B':
            if word:
                words.append(word)
            word = x
        else:
            if format == "text":
                word += (u'_' + x)
            else:
                word += (u' ' + x)
    if word:
        words.append(word)
    if format == "text":
        return u' '.join(words)
    else:
        return words


def sample_test(text):
    print(tokenize(text, format="text"))
    # from pyvi.pyvi import ViTokenizer
    # print ViTokenizer.tokenize(text)
    #
    # from underthesea import word_sent
    # print word_sent(text, format="text")


if __name__ == '__main__':
    texts = [
        "Chúng tôi là nhóm underthesea!"
    ]
    for text in texts:
        sample_test(text)
