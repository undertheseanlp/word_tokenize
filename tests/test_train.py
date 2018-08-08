# Preprocess data
#   python util/preprocess_vlsp2016.py --sample 100 --output util/vslp2016_100
# before run tests

from os.path import dirname, join
from unittest import TestCase

from util.crf.train import train

TMP_FOLDER = join(dirname(dirname(__file__)), "tmp")


class TestTrain(TestCase):
    def test_train(self):
        train_path = join(TMP_FOLDER, "vlsp2016_100", "train.txt")
        model_path = join(TMP_FOLDER, "test_model", "model.bin")
        train(train_path, model_path)
