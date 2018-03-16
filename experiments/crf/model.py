from languageflow.model.crf import CRF
from sklearn.model_selection import train_test_split

from experiments.crf.custom_transformer import CustomTransformer


class Model:
    def __init__(self, transformers):
        self.transformers = transformers

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
        self.transformers = transformer

    def load_data(self, sentences):
        self.sentences = sentences

    def fit_transform(self):
        template = [
            "T[-2].lower", "T[-1].lower", "T[0].lower", "T[1].lower", "T[2].lower",
            "T[-1].isdigit", "T[0].isdigit", "T[1].isdigit",

            "T[-1].istitle", "T[0].istitle", "T[1].istitle",

            "T[0,1].istitle", "T[0,2].istitle",

            "T[-2].is_in_dict", "T[-1].is_in_dict", "T[0].is_in_dict", "T[1].is_in_dict", "T[2].is_in_dict",

            "T[-2,-1].is_in_dict", "T[-1,0].is_in_dict", "T[0,1].is_in_dict", "T[1,2].is_in_dict",

            "T[-2,0].is_in_dict", "T[-1,1].is_in_dict", "T[0,2].is_in_dict",

            # word unigram and bigram and trigram
            "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
            "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
            "T[-2,0]", "T[-1,1]", "T[0,2]",
            # BI tag
            "T[-2][1]", "T[-1][1]"
        ]
        transformer = CustomTransformer(template)
        self.X, self.y = transformer.transform(self.sentences)

    def train(self):
        crf_params = {
            'c1': 1.0,  # coefficient for L1 penalty
            'c2': 1e-3,  # coefficient for L2 penalty
            'max_iterations': 1000,  #
            # include transitions that are possible, but not observed
            'feature.possible_transitions': True
        }
        X_train, X_dev, y_train, y_dev = train_test_split(self.X, self.y, test_size=0.1)
        model = CRF(params=crf_params)
        self.estimator = model.fit(X_train, y_train)
        y_pred = self.estimator.predict(X_dev)

