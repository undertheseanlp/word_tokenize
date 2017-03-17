
class DummyModel:
    def __init__(self):
        pass

    def predict(self, sentence):

        dictionary = open("simple_dict.txt", "r").read().splitlines()
        tokenized_words = [word.replace(" ", "_") for word in dictionary]
        s = sentence
        for word, tokenized_word in zip(dictionary, tokenized_words):
            if word in sentence:
                s = s.replace(word, tokenized_word)
        return s