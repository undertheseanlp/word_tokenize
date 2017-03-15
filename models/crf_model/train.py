# -*- coding: utf-8 -*-
import pycrfsuite
from os.path import dirname, join
from underthesea.corpus import PlainTextCorpus

from transformer import sent2labels, Transformer


def format_word(sentence):
    words = []
    for word in sentence.split(" "):
        if "_" in word:
            tokens = []
            word = word.replace("_", " ")
            for token in word.split(" "):
                tokens.append(token)

            for i in range(tokens.__len__()):
                if i != 0:
                    tokens[i] += "\tI_W"
                else:
                    tokens[i] += "\tB_W"
                words.append(tokens[i])
        elif word == "." or word == ",":
            words.append(word + "\t O")
        else:
            words.append(word + "\t B_W")
    return words


def list_to_tuple(sentences):
    word_tuple = []
    for i in sentences:
        arr = i.split('\t')
        word_tuple.append((arr[0], arr[1]))
    return word_tuple


def load_train_sents():
    corpus = PlainTextCorpus()
    file_path = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "output")
    corpus.load(file_path)
    sentences = []
    for document in corpus.documents:
        for sentence in document.sentences:
            if sentence != "":
                sentences.append(sentence)
    return sentences


train_sents = load_train_sents()
matrix = []
for sentence in train_sents:
    matrix.append(list_to_tuple(format_word(sentence)))
# new_matrix = []
# for j in matrix:
#     new_matrix.append(list_to_tuple(j))

train_sents = matrix

X_train = [Transformer.extract_features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

trainer = pycrfsuite.Trainer(verbose=False)
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

trainer.set_params({
    'c1': 1.0,  # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 1000,  # stop earlier

    # include transitions that are possible, but not observed
    'feature.possible_transitions': True
})
trainer.train("crf-model-1")
