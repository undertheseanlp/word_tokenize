import re

from languageflow.transformer.tagged_feature import functions


class TaggedTransformer:
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

    def word2features(self, s):
        features = []
        cached = {}
        for i, token in enumerate(s):
            tmp = []
            for template in self.templates:
                debug = True
                index1, index2, column, func, token_syntax = template
                cached_index1 = index1 + i
                cached_index2 = index2 + i if index2 else None
                cached_key = cached_index1, cached_index2, column, func
                if cached_key in cached:
                    result = cached[cached_key]
                else:
                    if debug:
                        prefix = "%s=" % token_syntax
                    else:
                        prefix = ""
                    if i + index1 < 0:
                        result = "%sBOS" % prefix
                        tmp.append(result)
                        continue
                    if i + index1 >= len(s):
                        result = "%sEOS" % prefix
                        tmp.append(result)
                        continue
                    if index2 is not None:
                        if i + index2 >= len(s):
                            result = "%sEOS" % prefix
                            tmp.append(result)
                            continue
                        tokens = [s[j][column] for j in range(i + index1, i + index2 + 1)]
                        word = " ".join(tokens)
                    else:
                        try:
                            word = s[i + index1][column]
                        except:
                            pass
                    if func is not None:
                        result = functions[func](word)
                    else:
                        result = word
                    cached[cached_key] = result
                result = "%s%s" % (prefix, result)
                tmp.append(result)
            features.append(tmp)
        return features

    def transform(self, sentences, contain_labels=False):
        X = [self.word2features(s) for s in sentences]
        if contain_labels:
            y = [self.sentence2labels(s) for s in sentences]
            return X, y
        return X

    def sentence2labels(self, s):
        return [row[-1] for row in s]