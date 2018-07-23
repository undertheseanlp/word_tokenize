from os import makedirs
from os.path import join, dirname
from languageflow.model.crf import CRF
from sklearn.model_selection import train_test_split
from sklearn_crfsuite import metrics

from .load_data import load_dataset
from .transformer.custom_transformer import CustomTransformer
from .feature_template import template


def train(train_path, model_path):
    print(train_path)
    train_set = []

    train_set += load_dataset(train_path)
    print("Load corpus from file", train_path)
    transformer = CustomTransformer(template)
    X, y = transformer.transform(train_set)

    # train
    crf_params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    X_train, X_dev, y_train, y_dev = train_test_split(X, y, test_size=0.01)
    folder = dirname(model_path)
    try:
        makedirs(folder)
    except:
        pass
    estimator = CRF(params=crf_params, filename=model_path)
    estimator.fit(X_train, y_train)
    y_pred = estimator.predict(X_dev)
    f1_score = metrics.flat_f1_score(y_dev, y_pred, average='weighted')
    print("Dev score: ", f1_score)


if __name__ == '__main__':
    train()
