from os.path import join, dirname
import joblib

from experiments.crf.score import multilabel_f1_score
from load_data import load_dataset
from model import word_tokenize
from sklearn_crfsuite import metrics

sentences = []
test_data = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", "test.txt")
sentences += load_dataset(test_data)
sentences = sentences[:100]
transformer = joblib.load(join(dirname(__file__), "model", "transformer.bin"))
X_test, y_test = transformer.transform(sentences)

y_predict, test_time = word_tokenize(sentences)
F1 = multilabel_f1_score(y_test, y_predict)
print("F1: ", F1)
print(0)
