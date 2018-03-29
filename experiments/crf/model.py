from os.path import join, dirname
from sklearn.model_selection import train_test_split
from languageflow.model.crf import CRF
import joblib

from score import multilabel_f1_score


class Model:
    def __init__(self, transformers):
        self.transformers = transformers

    def transform(self):
        raise Exception("Need implement")

    def train(self):
        raise Exception("Need implement")

    def export(self):
        raise Exception("Need implement")


class CRFModel(Model):
    def __init__(self, transformer):
        self.transformer = transformer

    def transform(self, sentences):
        self.X, self.y = self.transformer.transform(sentences)
        print(0)

    def train(self):
        crf_params = {
            'c1': 1.0,  # coefficient for L1 penalty
            'c2': 1e-3,  # coefficient for L2 penalty
            'max_iterations': 1000,  #
            # include transitions that are possible, but not observed
            'feature.possible_transitions': True
        }
        file_name = join(dirname(__file__), "models", "model.bin")
        X_train, X_dev, y_train, y_dev = train_test_split(self.X, self.y, test_size=0.01)
        self.estimator = CRF(params=crf_params, filename=file_name)
        self.estimator.fit(X_train, y_train)
        y_predict = self.estimator.predict(X_dev)
        f1 = multilabel_f1_score(y_dev, y_predict)
        print("dev score: ", f1)

    def export(self):
        joblib.dump(self.transformer, "models/transformer.bin")
