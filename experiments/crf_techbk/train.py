from __future__ import print_function
from sklearn.model_selection import train_test_split
from process import sent2features, sent2labels, sent2tokens
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from load_data import get_tokenizer
import time


###
# Bước 1: Lựa chọn mô hình (train + dev/ test)
# CRF1 -> model -> score1
# CRF2 -> model -> score2
# CRF1 + params1 -> model -> score3
# CRF2 + params2 -> model -> score4
# -> best_model (Estimator + Feature Selector)
# << model.py + interface Model >>


# Bước 2: Tạo file predict -> Train full trên toàn bộ dữ liệu (train + dev + test)
# Model -> best_model -> final_function
# -> 1: text -> Transformer -> vector
# -> 2: vector -> Estimator -> y
# -> 3: y -> Transformer -> y
# Benchmark final_function -> (F1 score + speed score)
###

def train_test(data=None):
    train_sents, dev_sents, test_sents = data or get_tokenizer()

    X_train = [sent2features(sent2tokens(s)) for s in train_sents]
    y_train = [sent2labels(s) for s in train_sents]

    print(len(X_train), len(y_train))

    X_dev = [sent2features(sent2tokens(s)) for s in dev_sents]
    y_dev = [sent2labels(s) for s in dev_sents]

    X_test = [sent2features(sent2tokens(s)) for s in test_sents]
    y_test = [sent2labels(s) for s in test_sents]

    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True,
        model_filename='model/model.bin'
    )
    crf.fit(X_train, y_train, X_dev=X_dev, y_dev=y_dev)
    start = time.time()
    y_pred = crf.predict(X_test)
    end = time.time()
    test_time = end - start
    F1 = metrics.flat_f1_score(y_test, y_pred, average='weighted')
    print("F1: ", F1)
    print("Test time: ", test_time)

    print(metrics.flat_classification_report(
        y_test, y_pred, digits=3
    ))


def train_full(data=None):
    data = data or get_tokenizer()
    train_sents, test_sents = train_test_split(data, test_size=0.2, shuffle=False)

    X_train = [sent2features(sent2tokens(s)) for s in data]
    y_train = [sent2labels(s) for s in data]

    X_test = [sent2features(sent2tokens(s)) for s in test_sents]
    y_test = [sent2labels(s) for s in test_sents]

    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True,
        model_filename='models/model.bin'
    )
    crf.fit(X_train, y_train)
    start = time.time()
    y_pred = crf.predict(X_test)
    end = time.time()
    test_time = end - start
    F1 = metrics.flat_f1_score(y_test, y_pred, average='weighted')
    print(F1)
    print("Test time: ", test_time)

    print(metrics.flat_classification_report(
        y_test, y_pred, digits=3
    ))


if __name__ == '__main__':
    data = get_tokenizer()
    train_test(data)
    # train_full(data)
