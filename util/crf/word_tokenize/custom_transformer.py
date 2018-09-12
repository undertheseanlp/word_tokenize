import re
from underthesea.feature_engineering.text import Text

from util.crf.word_tokenize.tagged_feature import template2features


class CustomTransformer:
    def __init__(self, templates=None):
        self.templates = [self._extract_template(template) for template in templates]

    def _extract_template(self, template):
        token_syntax = template
        matched = re.match(
            "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?",
            template)
        column = matched.group("column")
        column = int(column) if column else 0
        index1 = int(matched.group("index1"))
        index2 = matched.group("index2")
        index2 = int(index2) if index2 else None
        func = matched.group("function")
        return index1, index2, column, func, token_syntax

    def _word2features(self, s, i):
        features = [template2features(s, i, template) for template in self.templates]
        return features

    def sentence2features(self, s):
        output = [self._word2features(s, i, self.template) for i in
                  range(len(s))]
        return output

    def transform(self, sentences):
        X = [self.sentence2features(s) for s in sentences]
        y = 0
        # y = [self.sentence2labels(s) for s in sentences]
        return X, y

    def sentence2features(self, s):
        return [self._word2features(s, i) for i in range(len(s))]

    def sentence2labels(self, s):
        return [row[-1] for row in s]
