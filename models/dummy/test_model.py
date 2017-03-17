# -*- coding: utf-8 -*-

from unittest import TestCase
from model import DummyModel

class TestDummyModel(TestCase):
    def test_predict(self):
        input = "tôi đi học"
        output = "tôi đi_học"
        model = DummyModel()
        actual = model.predict(input)
        self.assertEqual(output, actual)

    def test_predict_2(self):
        input = "đặt vấn đề"
        output = "đặt vấn_đề"
        model = DummyModel()
        actual = model.predict(input)
        self.assertEqual(output, actual)
