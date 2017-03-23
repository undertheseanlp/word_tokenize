# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join

import matplotlib.pyplot as plt
import time

from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from underthesea.corpus import PlainTextCorpus

from models.crf_model.confusion_matrix import Confution_Matrix
from pipelines.compare_dictionary import compare_dictionary
from underthesea.corpus import viet_dict_11K


def to_column(sentence):
    words = []
    result = []
    path = join(dirname(__file__), "logs", "punctuation.txt")
    punctuations = open(path, "r").read().split("\n")
    for punctuation in punctuations:
        punctuation = unicode(punctuations)
    for word in sentence.split(" "):
        words.append(word)
    if words[0] == "":
        words.pop(0)
    for word in words:
        tokens = []
        if word in punctuations:
            result.append((word, "O"))
        else:
            for token in word.split("_"):
                tokens.append(token)
            for i in range(len(tokens)):
                if i == 0:
                    if tokens[i] != "":
                        result.append((tokens[i], "BW"))
                else:
                    result.append((tokens[i], "IW"))
    return result


def count_token(documents):
    count = 0
    for document in documents:
        for sentences in document.sentences:
            for word in sentences.split(' '):
                count += 1
    return count


if __name__ == '__main__':
    OPTIONS = {
        "F1_Score": True,
        "Confusion matrix": True,
        "Error Analysis": True,
        "Time Speed": True
    }
    time_start = time.time()
    model_name = "output_crf"
    output_folder = join(dirname(dirname(__file__)), "data", "corpus", "test", "output")
    model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "test", model_name)
    expected_corpus = PlainTextCorpus()
    expected_corpus.load(output_folder)
    actual_corpus = PlainTextCorpus()
    actual_corpus.load(model_output_folder)
    actual_column = []
    predict_column = []
    actual_label = []
    predict_label = []
    for e, a in zip(expected_corpus.documents, actual_corpus.documents):
        for i, j in zip(e.sentences, a.sentences[:-1]):
            predict_column.append(to_column(i))
            actual_column.append(to_column(j))
    for x, y in zip(predict_column, actual_column):
        for i, j in zip(x, y):
            predict_label.append(i[1])
            actual_label.append(j[1])
    if OPTIONS["F1_Score"]:
        f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
        f1 = f1_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
        precision = precision_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
        recall = recall_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
        x = f.read().split('\n')
        x[0] = "F1 = %0.2f percent" % f1
        x[1] = "Precision = %0.2f percent" % precision
        x[2] = "Recall = %0.2f percent" % recall
        x = x[:-1]
        f.close()
    if OPTIONS["Confusion matrix"]:
        f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
        confusion_matrix = confusion_matrix(actual_label, predict_label, labels=["BW", "IW", "O"])
        x = f.read().split('\n')
        x[6] = "BW\t" + str(confusion_matrix[0][0]) + "\t" + str(confusion_matrix[0][1]) + "\t\t" + str(
            confusion_matrix[0][2])
        x[7] = "IW\t" + str(confusion_matrix[1][0]) + "\t" + str(confusion_matrix[1][1]) + "\t" + str(
            confusion_matrix[1][2])
        x[8] = "O\t" + str(confusion_matrix[2][0]) + "\t\t" + str(confusion_matrix[2][1]) + "\t\t" + str(
            confusion_matrix[2][2])
        plt.figure()
        class_name = ["BW", "IW", "O"]
        Confution_Matrix.plot_confusion_matrix(confusion_matrix, classes=class_name,
                                               title='Confusion matrix')
        plt.savefig('confusion matrix.png')
        plt.show()
        x = x[:-1]
        f.close()
    if OPTIONS["Error Analysis"]:
        f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
        (new_word, word_in_dictionary) = compare_dictionary(model_output_folder)
        x = f.read().split('\n')
        x[12] = "- Word in dictionary: %d" % len(word_in_dictionary)
        x[13] = "- New Word : %d" % len(new_word)
        coverage = float(len(new_word)) / float(len(viet_dict_11K.words))
        x[14] = "- Word Coverage : %0.2f" % coverage
        x = x[:-1]
        f.close()
    if OPTIONS["Time Speed"]:
        f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r+')
        x = f.read().split("\n")
        time_stop = time.time()
        time_per_token = (time_stop - time_start) / float(count_token(actual_corpus.documents))
        time_per_token = 1.00 / time_per_token
        x[17] = "Time speed: %0.6f token per second" % time_per_token
        x = x[:-1]
        f.close()
    f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'w')
    for i in x:
        f.write(i + "\n")
    f.close()
