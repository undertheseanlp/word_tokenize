# -*- coding: utf-8 -*-
from unittest import TestCase

from transformer import Transformer


class TestTransformer(TestCase):
    def test_transform(self):
        sentence = u"tôi đi học"
        result = Transformer.transform(sentence)
        print 0

    def test_extract_features(self):
        sentence = [
            (u"tôi",),
            (u"đi",),
            (u"học",)
        ]
        result = Transformer.extract_features(sentence)
        print 0
