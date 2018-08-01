from os import makedirs
from os.path import join, dirname
from languageflow.model.crf import CRF

from .load_data import load_dataset
from .transformer.custom_transformer import CustomTransformer
from .feature_template import template


def train(train_path, model_path):
    train_set = []

    train_set += load_dataset(train_path)
    print("Load data from file", train_path)
    transformer = CustomTransformer(template)
    X, y = transformer.transform(train_set)

    # train
    params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    folder = dirname(model_path)
    try:
        makedirs(folder)
    except:
        pass
    estimator = CRF(params=params, filename=model_path)
    estimator.fit(X, y)

def train_test(train_path, test_path):
    print(0)