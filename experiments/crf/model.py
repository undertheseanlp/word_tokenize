import joblib
from sklearn.model_selection import train_test_split
from sklearn_crfsuite import CRF

from score import multilabel_f1_score


class Model:
    def __init__(self, transformer):
        self.transformer = transformer

    def load_data(self):
        raise Exception("Need implement")

    def fit_transform(self):
        raise Exception("Need implement")

    def train(self):
        raise Exception("Need implement")

    def evaluate(self):
        raise Exception("Need implement")


class CRFModel(Model):
    def __int__(self, transformer):
        self.transformer = transformer

    def load_data(self, sentences):
        self.sentences = sentences

    def fit_transform(self):
        self.X, self.y = self.transformer.transform(self.sentences)

    def train(self):
        # crf_params = {
        #     'c1': 1.0,  # coefficient for L1 penalty
        #     'c2': 1e-3,  # coefficient for L2 penalty
        #     'max_iterations': 1000,  #
        #     # include transitions that are possible, but not observed
        #     'feature.possible_transitions': True
        # }
        X_train, X_dev, y_train, y_dev = train_test_split(self.X, self.y, test_size=0.1)
        model = CRF(c1=1.0, c2=1e-3, max_iterations=1000)
        self.estimator = model.fit(X_train, y_train)
        y_pred = self.estimator.predict(X_dev)
        score = multilabel_f1_score(y_dev, y_pred)
        print("F1 Score: ", score)

    def export(self):
        joblib.dump(self.estimator, "crf-model.bin")

