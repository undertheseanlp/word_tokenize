#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from six import u, print_


class WordPatternFeature(object):
    """Generates a feature that describes the word pattern of a feature.
    A word pattern is a rough representation of the word, examples:
        original word | word pattern
        ----------------------------
        John          | Aa+
        Washington    | Aa+
        DARPA         | A+
        2055          | 9+
    """

    def __init__(self):
        """Instantiates a new object of this feature generator."""
        # maximum length of tokens after which to simply cut off
        self.max_length = 15
        # if cut off because of maximum length, use this char at the end of the word to signal
        # the cutoff
        self.max_length_char = "~"

        self.normalization = [
            (u"""[ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀẢÃẠĂẮẶẰẲẴÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ]""", "A"),
            (u"""[abcdefghijklmnopqrstuvwxyzáàảãạăắặằẳẵâấầẩẫậđéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ]""", "a"),
            (r"[0-9]", "9"),
            (r"[\.\!\?\,\;]", "."),
            (r"[\(\)\[\]\{\}]", "("),
            (r"[^Aa9\.\(]", "#")
        ]

        # note: we do not map numers to 9+, e.g. years will still be 9999
        self.mappings = [
            (r"[A]{2,}", "A+"),
            (r"[a]{2,}", "a+"),
            (r"[\.]{2,}", ".+"),
            (r"[\(]{2,}", "(+"),
            (r"[#]{2,}", "#+")
        ]

    def convert_window(self, window):
        """Converts a Window object into a list of lists of features, where features are strings.
        Args:
            window: The Window object (defined in datasets.py) to use.
        Returns:
            List of lists of features.
            One list of features for each token.
            Each list can contain any number of features (including 0).
            Each feature is a string.
        """
        result = []
        for token in window.tokens:
            result.append(["wp=%s" % (self.token_to_wordpattern(token))])
        return result

    def token_to_wordpattern(self, word):
        """Converts a token/word to its word pattern.
        Args:
            token: The token/word to convert.
        Returns:
            The word pattern as string.
        """
        normalized = word
        for from_regex, to_str in self.normalization:
            normalized = re.sub(from_regex, to_str, normalized)

        wpattern = normalized
        for from_regex, to_str in self.mappings:
            wpattern = re.sub(from_regex, to_str, wpattern)

        if len(wpattern) > self.max_length:
            wpattern = wpattern[0:self.max_length] + self.max_length_char

        return wpattern


WORD_PATTERN = WordPatternFeature()


if __name__ == '__main__':

    w_pattern_creator = WordPatternFeature()
    words = u'ĐÂY ( Đây ) đây Rồi [ MMánh khai@gmail.com ]'.split(' ')
    for word in words:
        print_(w_pattern_creator.token_to_wordpattern(word))
