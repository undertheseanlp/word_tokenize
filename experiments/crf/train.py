from os.path import dirname, join
from sklearn.model_selection import train_test_split
from languageflow.model.crf import CRF

from custom_transformer import CustomTransformer
from feature_template import template
from load_data import load_dataset
from score import multilabel_f1_score

if __name__ == '__main__':
    # =========================================================================#
    #                               Data
    # =========================================================================#

    sentences = []
    for f in ["train.txt", "dev.txt", "test.txt"]:
        file = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", f)
        sentences += load_dataset(file)
        sentences = sentences[:1000]

    # =========================================================================#
    #                                Transformer
    # =========================================================================#

    transformer = CustomTransformer(template)
    X, y = transformer.transform(sentences)
    X_train, X_dev, y_train, y_dev = train_test_split(X, y, test_size=0.1)

    # =========================================================================#
    #                               Models
    # =========================================================================#

    crf_params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    model_file = join(dirname(__file__), "model.bin")
    estimator = CRF(params=crf_params, filename=model_file)
    estimator.fit(X_train, y_train)

    # =========================================================================#
    #                              Evaluation
    # =========================================================================#

    y_pred = estimator.predict(X_dev)
    f1_score = multilabel_f1_score(y_dev, y_pred)
    print(f1_score)
