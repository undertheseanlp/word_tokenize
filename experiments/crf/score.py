from sklearn.metrics import f1_score


def _flat(l):
    """
    :type l: list of list
    """
    return [item[0] for item in l]


def score(y_true, y_pred):
    y_pred = _flat(y_pred)
    y_true = _flat(y_true)
    print("F1 :", f1_score(y_true, y_pred))
