# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join

import matplotlib.pyplot as plt
import time

from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from underthesea.corpus import PlainTextCorpus

from labs.computeF1.to_column import to_column
from models.crf_model.confusion_matrix import Confution_Matrix
from pipelines.compare_dictionary import compare_dictionary
from underthesea.corpus import viet_dict_11K


def count_token(documents):
    count = 0
    for document in documents:
        for sentences in document.sentences:
            for word in sentences.split(' '):
                count += 1
    return count


if __name__ == '__main__':
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
    f = open(join(dirname(__file__), 'logs', 'crf', 'result.txt'), 'r', 'w')
    for e, a in zip(expected_corpus.documents, actual_corpus.documents):
        for i, j in zip(e.sentences, a.sentences[:-1]):
            predict_column.append(to_column(i))
            actual_column.append(to_column(j))
    for x, y in zip(predict_column, actual_column):
        for i, j in zip(x, y):
            predict_label.append(i[1])
            actual_label.append(j[1])
    print "1.   update F1 score"
    print "2.   update confusion matrix"
    print "3.   update Word Analysis"
    print "4.   Update time speed"
    choose = int(raw_input("what do u want :"))
    if choose == 1:
        f.read().split('\n')
        print "Accuracy = %0.2f percent" % (
            accuracy_score(actual_label, predict_label) * 100)
    # print "confusion matrix: \n"
    if choose == 2:
        confusion_matrix = confusion_matrix(actual_label, predict_label, labels=["BW", "IW", "O"])
        f.write("Confusion matrix : \n")
        f.write("\tBW\t\tIW\t\tO\n")
        f.write(
            "BW\t" + str(confusion_matrix[0][0]) + "\t" + str(confusion_matrix[0][1]) + "\t\t" + str(
                confusion_matrix[0][2]) + "\n")
        f.write(
            "IW\t" + str(confusion_matrix[1][0]) + "\t" + str(confusion_matrix[1][1]) + "\t" + str(
                confusion_matrix[1][2]) + "\n")
        f.write("O\t" + str(confusion_matrix[2][0]) + "\t\t" + str(confusion_matrix[2][1]) + "\t\t" + str(
            confusion_matrix[2][2]) + "\n")

        plt.figure()
        class_name = ["BW", "IW", "O"]
        Confution_Matrix.plot_confusion_matrix(confusion_matrix, classes=class_name,
                                               title='Confusion matrix')
        plt.savefig('confusion matrix.png')
        plt.show()
        f.write("\n\n")
    if choose == 3:
        (new_word, word_in_dictionary) = compare_dictionary(model_output_folder)
        f.write("Word Analysis: \n")
        f.write("- Word in dictionary : %d\n" % len(word_in_dictionary))
        f.write("- New Word : %d\n" % len(new_word))
        coverage = float(len(new_word)) / float(len(viet_dict_11K.words))
        f.write("- Word Coverage : %0.2f\n" % coverage)
        f.write("\n\n")
    if choose == 4:
        time_stop = time.time()
        time_per_token = (time_stop - time_start) / float(count_token(actual_corpus.documents))
        f.write("Time speed: %0.6f second per token\n" % time_per_token)
    print 0
