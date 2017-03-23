import re
from os.path import dirname, join

import pycrfsuite

from transformer import Transformer
from underthesea.corpus import viet_dict_22K


class CRFModel:
    def __init__(self):
        self.model = pycrfsuite.Tagger()
        self.model.open("crf-model-1")
        self.words = viet_dict_22K.words
        path = join(dirname(dirname(dirname(__file__))), "pipelines", "logs", "punctuation.txt")
        self.punctuation = open(path, "r").read().split("\n")

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
        # tokenized_sentence = tokenized_sentence[:-1]
        format_sentcence = ''
        for word in tokenized_sentence.split("_"):
            if word not in self.punctuation:
                format_sentcence += word[: -1] + "_"
        tokenized_sentence = format_sentcence[:-1]
        # use dictionary vietdict 11k
        dictionary = [word for word in self.words if re.search(" $", word) is None]
        dictionary_tokenizeds = [word.replace(" ", "_") for word in dictionary]
        for word, dictionary_tokenized in zip(dictionary, dictionary_tokenizeds):
            if word in tokenized_sentence:
                tokenized_sentence = tokenized_sentence.replace(word, dictionary_tokenized)
        return tokenized_sentence
