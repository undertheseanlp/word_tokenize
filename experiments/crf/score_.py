def precision(y_true, y_pred):
    labels_true = set(y_true).intersection(y_pred)
    if len(y_pred) == 0:
        return 0
    else:
        return len(labels_true) / len(y_pred)


def recall(y_true, y_pred):
    labels_true = set(y_true).intersection(y_pred)
    return len(labels_true) / len(y_pred)


def f1_score(y_true, y_pred):
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * (p * r) / (p + r)
