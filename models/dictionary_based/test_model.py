# -*- coding: utf-8 -*-

from unittest import TestCase
from model import DictionaryModel

class TestDummyModel(TestCase):
    def setUp(self):
        self.model = DictionaryModel()

    def test_predict(self):
        input = "gia tăng số trường đại học đến 300 trường ( 2015 ) , và 450 trường ( năm 2020 ) ."
        output = "gia_tăng số trường đại_học đến 300 trường ( 2015 ) , và 450 trường ( năm 2020 ) ."
        actual = self.model.predict(input)
        # print actual.decode("utf-8")
        self.assertEqual(output, actual)

if __name__ == '__main__':
    input = "gia tăng số trường đại học đến 300 trường ( 2015 ) , và 450 trường ( năm 2020 ) ."
    output = " gia_tăng số trường đại_học đến 300 trường ( 2015 ) , và 450 trường ( năm 2020 ) ."
    model = DictionaryModel()
    actual = model.predict(input)
    print actual.decode("utf-8")

