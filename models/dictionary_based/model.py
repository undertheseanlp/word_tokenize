import re
from os.path import dirname, join
from os import listdir
from underthesea.corpus import viet_dict_11K


class DictionaryModel:
    def __init__(self):
        pass

    def predict(self, sentence):
        words = viet_dict_11K.words
        dictionary = [word for word in words if re.search(" $", word) is None]

        tokenized_words = [word.replace(" ", "_") for word in dictionary]
        s = sentence
        for word, tokenized_word in zip(dictionary, tokenized_words):
            if word in sentence:
                s = s.replace(word, tokenized_word)
        return s
