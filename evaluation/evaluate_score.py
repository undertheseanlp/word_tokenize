from os.path import join, dirname
import joblib
import pycrfsuite
from sklearn_crfsuite import metrics

from experiments.crf_2.load_data import load_dataset


sentences = []
test_data = join(dirname(dirname(__file__)), "data", "vlsp2016", "corpus", "test.txt")
sentences += load_dataset(test_data)
path_transformer = join(dirname(dirname(__file__)), "experiments", "crf_2", "model", "transformer.bin")
path_model = join(dirname(dirname(__file__)), "experiments", "crf_2", "model", "model.bin")
transformer = joblib.load(path_transformer)
X_test, y_test = transformer.transform(sentences)

estimator = pycrfsuite.Tagger()
estimator.open(path_model)
y_predict = [estimator.tag(x) for x in X_test]
f1 = metrics.flat_f1_score(y_test, y_predict, average='weighted')
print("F1 score: ", f1)
