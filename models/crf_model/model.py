import re
from os.path import dirname, join
from os import listdir

import pycrfsuite

from transformer import Transformer


class CRFModel:
    def __init__(self):
        self.model = pycrfsuite.Tagger()
        self.model.open("crf-model-1")

    def predict(self, sentence):
        sentence = Transformer.transform(sentence)
        tags = self.model.tag(sentence)
        tokenized_sentence = u''
        for tag, word in zip(tags, sentence):
            word = word[0]
            if tag == "I_W":
                tokenized_sentence = tokenized_sentence + u"_" + word
            else:
                tokenized_sentence = tokenized_sentence + word
            tokenized_sentence += " "
        format_sentcence = ''
        for word in tokenized_sentence.split("_"):
            format_sentcence += word[: -1] + "_"
        tokenized_sentence = format_sentcence[:-1]

        return tokenized_sentence


