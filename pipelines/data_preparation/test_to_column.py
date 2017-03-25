# -*- coding: utf-8 -*-
from unittest import TestCase

from to_column import to_column


class TestTo_column(TestCase):
    def test_to_column_1(self):
        sentence = "A B C D"
        tagged_column = to_column(sentence)
        tagged_actual = [[('A', 'BW')], [('B', 'BW')], [('C', 'BW')], [('D', 'BW')]]
        self.assertEqual(tagged_column, tagged_actual)

    def test_to_column_2(self):
        sentence = "A B , C D"
        tagged_column = to_column(sentence)
        tagged_actual = [[('A', 'BW')], [('B', 'BW')], [(',', 'O')], [('C', 'BW')], [('D', 'BW')]]
        self.assertEqual(tagged_column, tagged_actual)

    def test_to_column_3(self):
        sentence = "A_B . , C_D ; "
        tagged_column = to_column(sentence)
        tagged_actual = [[('A', 'BW'), ('B', 'IW')], [('.', 'O')], [(',', 'O')], [('C', 'BW'), ('D', 'IW')],
                         [(';', 'O')]]
        self.assertEqual(tagged_column, tagged_actual)

    def test_to_column_4(self):
        sentence = "abc@123 456"
        tagged_column = to_column(sentence)
        tagged_actual = [[('abc@123', 'BW')], [('456', 'BW')]]
        self.assertEqual(tagged_column, tagged_actual)

    def test_to_column_5(self):
        sentence = "A : B 1_C D"
        tagged_column = to_column(sentence)
        tagged_actual = [[('A', 'BW')], [(':', 'O')], [('B', 'BW')], [('1', 'BW'), ('C', 'IW')], [('D', 'BW')]]
        self.assertEqual(tagged_column, tagged_actual)

    def test_to_column_6(self):
        sentence = "A : B 1_C D"
        tagged_column = to_column(sentence)
        tagged_actual = [[('A', 'BW')], [(':', 'O')], [('B', 'BW')], [('1', 'BW'), ('C', 'IW')], [('D', 'BW')]]
        self.assertEqual(tagged_column, tagged_actual)
