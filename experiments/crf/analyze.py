from os.path import join, dirname
import time
import joblib
import pycrfsuite
from sklearn_crfsuite import metrics

from load_data import load_dataset


transformer = joblib.load(join(dirname(__file__), "model", "transformer.bin"))
path = join(dirname(__file__), "model", "model.bin")
estimator = pycrfsuite.Tagger()
estimator.open(path)

test_set = load_dataset(join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", "test.txt"))
X_test, y_test = transformer.transform(test_set)
start = time.time()
y_pred = [estimator.tag(x) for x in X_test]
end = time.time()
test_time = end - start
f1_test_score = metrics.flat_f1_score(y_test, y_pred, average='weighted')
print("F1 score: ", f1_test_score)
print("Test time: ", test_time)
with open("report.txt", "w") as f:
    f.write("F1 score: " + str(f1_test_score) + "\n" + "Test time: " + str(test_time))
