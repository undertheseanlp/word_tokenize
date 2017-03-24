# -*- coding: utf-8 -*-
from unittest import TestCase
from model import CRFModel
from transformer import Transformer


class TestCRFModel(TestCase):
    def test_predict(self):
        model = CRFModel()

        sentence = u"Hươu là loài vật được con người thuần dưỡng đã hàng trăm năm ."

        output = u"Hươu là loài_vật được con_người thuần_dưỡng đã hàng trăm năm ."

        tokenized_sentence = model.predict(sentence)
        self.assertEquals(tokenized_sentence, output)
        print 0

    def test_predict2(self):
        model = CRFModel()
        sentence = u"tuy nhiên , trong quá trình này cũng bộc lộ một số vấn đề về môi trường bao gồm cả môi trường tự nhiên và môi trường xã hội ."
        output = u"a"
        tokenized_sentence = model.predict(sentence)
        self.assertEquals(tokenized_sentence, output)
