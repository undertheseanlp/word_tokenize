from sklearn.metrics import f1_score


def score(y_true, y_pred):
    f1 = sum([f1_score(y_true[i], y_pred[i], average='weighted') for i in range(len(y_pred))])/len(y_pred)
    return f1
