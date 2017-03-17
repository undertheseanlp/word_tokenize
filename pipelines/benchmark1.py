# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from underthesea.corpus import PlainTextCorpus

from labs.computeF1.to_column import to_column
from labs.copare_sentence_1.script import compare_sentence_1


def column_to_label(column):
    label = []
    for x in column:
        for i in x:
            label.append(i[1])
    return label


if __name__ == '__main__':
    model_name = "output_crf"
    output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output")
    model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", model_name)
    expected_corpus = PlainTextCorpus()
    expected_corpus.load(output_folder)
    actual_corpus = PlainTextCorpus()
    actual_corpus.load(model_output_folder)
    actual_column = []
    predict_column = []
    actual_label = []
    predict_label = []
    f = open(join(dirname(__file__), "logs", "crf", "result.txt"), "w")
    for e, a in zip(expected_corpus.documents, actual_corpus.documents):
        for i, j in zip(e.sentences, a.sentences[:-1]):
            if i != j:
                f.write(i.encode('utf-8') + "\n" + j.encode('utf-8') + "\n \n")
                total_fail = compare_sentence_1(i, j)
                for k in total_fail:
                    f.write(k[0].encode('utf-8') + " :" + k[1].encode('utf-8') + "->" +
                            k[2].encode('utf-8') + "\n")
                f.write("\n")
            predict_column.append(to_column(i))
            actual_column.append(to_column(j))
        for x, y in zip(predict_column, actual_column):
            for i, j in zip(x, y):
                predict_label.append(i[1])
                actual_label.append(j[1])

    print "F1 = %0.2f percent" % (
        f1_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100)
    print "Precision = %0.2f percent" % (
        precision_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100)
    print "Recall = %0.2f percent" % (
        recall_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100)
    print "Accuracy = %0.2f percent" % (
        accuracy_score(actual_label, predict_label) * 100)
