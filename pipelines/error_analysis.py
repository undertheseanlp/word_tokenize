from os.path import dirname
from os.path import join
from labs.computeF1.to_column import to_column
from underthesea.corpus import PlainTextCorpus

from labs.compare_sentence_1.column_to_logs import word2column
from labs.compare_sentence_1.script import compare_sentence


def format_to_list(formated):
    list = []
    for x in formated:
        for y in x:
            list.append(y)
    return list


model_name = "output_crf"
output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output")
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", model_name)

expected_corpus = PlainTextCorpus()
expected_corpus.load(output_folder)
actual_corpus = PlainTextCorpus()
actual_corpus.load(model_output_folder)
total_result = []
total_expected = []
total_actual = []
for e, a in zip(expected_corpus.documents, actual_corpus.documents):
    for i, j in zip(e.sentences, a.sentences[:-1]):
        if i != j:
            total_result.append(compare_sentence(i, j))
for result in total_result:
    for i in range(len(result)):
        total_actual.append(result[i][0])
        total_expected.append(result[i][1])
expected_column = []
actual_column = []
for x, y in zip(total_actual, total_expected):
    expected_column.append(to_column(y))
    actual_column.append(to_column(x))
expected_column = format_to_list(expected_column)
actual_column = format_to_list(actual_column)
f1 = open(join(dirname(__file__), "logs", "crf", "fail_BW.txt"), "w")
f2 = open(join(dirname(__file__), "logs", "crf", "fail_IW.txt"), "w")
f3 = open(join(dirname(__file__), "logs", "crf", "fail_O.txt"), "w")
for (x, y) in zip(expected_column, actual_column):
    if x[1] == "BW" and y[1] == "IW":
        # print x[0] + ": " + x[1] + '->' + y[1] + '\n'
        f1.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
    if x[1] == "BW" and y[1] == "O":
        f1.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
    if x[1] == "IW" and y[1] == "BW":
        f2.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
    if x[1] == "IW" and y[1] == "O":
        f2.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
    if x[1] == "O" and y[1] == "BW":
        f3.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
    if x[1] == "O" and y[1] == "IW":
        f3.write(x[0].encode('utf-8') + ' -> ' + y[0].encode('utf-8') + "( %s )" % y[
            1].encode('utf-8') + '\n')
