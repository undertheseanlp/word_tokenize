from os.path import join, dirname
from os import mkdir

from sklearn.metrics import f1_score
from underthesea.corpus import PlainTextCorpus
from pipelines import model_name
from models.crf_2.to_colum import to_column
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def get_data():
    output_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus_2", "test", "output")
    model_output_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus_2", "test", "output_%s" % model_name)
    expected_corpus = PlainTextCorpus()
    expected_corpus.load(output_folder)
    actual_corpus = PlainTextCorpus()
    actual_corpus.load(model_output_folder)
    return expected_corpus, actual_corpus


def get_score():
    expected_corpus, actual_corpus = get_data()
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
    f1 = f1_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
    precision = precision_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
    recall = recall_score(actual_label, predict_label, list(set(actual_label)), 1, 'weighted', None) * 100
    print "F1 = %.2f percent" % f1
    print "Precision = %.2f" % precision
    print "Recall = %.2f percent" % recall


if __name__ == '__main__':
    get_score()

