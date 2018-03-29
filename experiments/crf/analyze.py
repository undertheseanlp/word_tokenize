from os.path import join, dirname
import joblib

from load_data import load_dataset
from models import word_sent
from score import multilabel_f1_score


sentences = []
test_data = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", "test.txt")
sentences += load_dataset(test_data)

transformer = joblib.load(join(dirname(__file__), "models", "transformer.bin"))
X_test, y_test = transformer.transform(sentences)
y_predict, test_time = word_sent(sentences)
f1 = multilabel_f1_score(y_test, y_predict)
score = "f1 score: " + str(f1) + "\n" + "Test time: " + str(test_time)
with open("exported/score.txt", "w") as f:
    f.write(score)
print(score)
