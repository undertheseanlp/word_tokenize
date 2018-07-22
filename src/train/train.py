from __future__ import print_function
from sklearn.model_selection import train_test_split
from sklearn_crfsuite import metrics, CRF
from utils.helpers import save_data, load_data
from os.path import join
import time
import warnings
warnings.filterwarnings('ignore')


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

class CRFWrapper():

    def __init__(self, path):
        self.PATH = path  # 'data/vlsp2016/cleaned/'
        self.model = None

    def load(self):
        self.X_train = load_data(join(self.PATH, 'X_train.pkl'))
        self.y_train = load_data(join(self.PATH, 'y_train.pkl'))
        self.X_dev = load_data(join(self.PATH, 'X_dev.pkl'))
        self.y_dev = load_data(join(self.PATH, 'y_dev.pkl'))
        self.X_test = load_data(join(self.PATH, 'X_test.pkl'))
        self.y_test = load_data(join(self.PATH, 'y_test.pkl'))

    def fit(self):
        print('Start training model')
        self.load()
        self.model = CRF(
            algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100,
            all_possible_transitions=True,
        )
        self.model.fit(self.X_train, self.y_train, self.X_dev, self.y_dev)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        f1_score = metrics.flat_f1_score(self.y_test, y_pred, average='weighted')
        print('F1 score: {:.4f}'.format(f1_score))
        print(metrics.flat_classification_report(
            self.y_test, y_pred, digits=4
        ))

    def save(self):
        save_data(self.model, 'model/model.bin')

    def execute(self):
        self.fit()
        self.evaluate()
        self.save()

        # def train_full(data=None):
        #     data = data or get_tokenizer()
        #     train_sents, test_sents = train_test_split(data, test_size=0.2, shuffle=False)

        #     X_train = [sent2features(sent2tokens(s)) for s in data]
        #     y_train = [sent2labels(s) for s in data]

        #     X_test = [sent2features(sent2tokens(s)) for s in test_sents]
        #     y_test = [sent2labels(s) for s in test_sents]

        #     crf = sklearn_crfsuite.CRF(
        #         algorithm='lbfgs',
        #         c1=0.1,
        #         c2=0.1,
        #         max_iterations=100,
        #         all_possible_transitions=True,
        #         model_filename='models/model.bin'
        #     )
        #     crf.fit(X_train, y_train)
        #     start = time.time()
        #     y_pred = crf.predict(X_test)
        #     end = time.time()
        #     test_time = end - start
        #     F1 = metrics.flat_f1_score(y_test, y_pred, average='weighted')
        #     print(F1)
        #     print("Test time: ", test_time)

        #     print(metrics.flat_classification_report(
        #         y_test, y_pred, digits=3
        #     ))

        # if __name__ == '__main__':
        #     data = get_tokenizer()
        #     train_test(data)
        # train_full(data)
