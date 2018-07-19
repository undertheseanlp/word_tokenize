from src.process import sent2features, sent2labels, sent2tokens
from src.load_data import DataLoader
from utils.helpers import save_data
from os.path import join


class DataTransformer():

    SAVE_PATH = 'data/vlsp2016/cleaned/'

    def __init__(self):
        pass

    def load(self):
        train_sents, dev_sents, test_sents = DataLoader().get_tokenizer()
        return (train_sents, dev_sents, test_sents)

    def transform(self, data):
        X = [sent2features(sent2tokens(sent)) for sent in data]
        y = [sent2labels(sent) for sent in data]
        return X, y

    def execute(self, save=True):
        train, dev, test = self.load()
        X_train, y_train = self.transform(train)
        X_dev, y_dev = self.transform(dev)
        X_test, y_test = self.transform(test)

        if save:
            save_data(X_train, join(self.SAVE_PATH, 'X_train.pkl'))
            save_data(y_train, join(self.SAVE_PATH, 'y_train.pkl'))
            save_data(X_test, join(self.SAVE_PATH, 'X_test.pkl'))
            save_data(y_test, join(self.SAVE_PATH, 'y_test.pkl'))
            save_data(X_dev, join(self.SAVE_PATH, 'X_dev.pkl'))
            save_data(y_dev, join(self.SAVE_PATH, 'y_dev.pkl'))
        # return (X_train, y_train, X_dev, y_dev, X_test, y_test)
