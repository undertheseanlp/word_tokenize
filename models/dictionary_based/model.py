import re


class DictionaryModel:
    def __init__(self):
        pass

    def predict(self, sentence):
        dictionary = open("vn_words\\Viet74K.txt", "r").read().splitlines()
        dictionary = [word for word in dictionary if re.search(" $", word) is None]
        tokenized_words = [word.replace(" ", "_") for word in dictionary]
        s = sentence
        for word, tokenized_word in zip(dictionary, tokenized_words):
            if word in sentence:
                s = s.replace(word, tokenized_word)
        return s
