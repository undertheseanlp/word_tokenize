class Tranformer:
    def __init__(self, filename):
        punctuation = open(filename, "r").read()

    def to_column(self, documents):
        for document in documents:
            for sentences in document.sentences:
                print 0

    def sentence_to_column(self, sentence):
        return_sentence = []
        for word in sentence.split(' '):
            if word in self.punctuation:
                return_sentence.append((word, "O"))
            if '_' in word:
                tokens = []
                for token in word.split('_'):
                    tokens.append(token)
                for i in range(len(tokens)):
                    if i == 0:
                        return_sentence.append((tokens[0], "BW"))
                    else:
                        return_sentence.append((tokens[i], "IW"))
            else:
                return_sentence.append((word, "IW"))
        return return_sentence
