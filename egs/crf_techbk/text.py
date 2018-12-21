# -*- coding: utf-8 -*-
import unicodedata
import sys
import re
import six


def Text(text):
    """ provide a wrapper for python string
    map byte to str (python 3)
    map str to unicode (python 2)
    all string in utf-8 encoding
    normalize string to NFC
    """
    if not is_unicode(text):
        text = text.decode("utf-8")
    text = unicodedata.normalize("NFC", text)
    return text


def is_unicode(text):
    if sys.version_info >= (3, 0):
        unicode_type = str
    else:
        unicode_type = unicode
    return type(text) == unicode_type


def create_patterns():
    specials = ["==>", "->", "\.\.\.", ">>"]
    digit = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    datetime = [
        "\d{1,2}\/\d{1,2}(\/\d+)?",
        "\d{1,2}-\d{1,2}(-\d+)?",
    ]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]

    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(specials)
    patterns.extend([web, email])
    patterns.extend(datetime)
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    # if sys.version_info < (3, 0):
    if six.PY2:
        patterns = patterns.decode('utf-8')
    return patterns


__PATTERNS__ = create_patterns()


def sylabelize(text):
    """
    sylabelize text for word segmentation

    :param text: raw text input
    :return: sylabelize text
    """
    text = Text(text)
    tokens = re.findall(__PATTERNS__, text, re.UNICODE)
    return ["%s" % token[0].strip(' ') for token in tokens]


def normalization(text):
    words = sylabelize(text)
    return u' '.join(words)
