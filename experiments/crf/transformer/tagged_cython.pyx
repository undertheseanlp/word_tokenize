import re
from os.path import join, dirname
from languageflow.reader.dictionary_loader import DictionaryLoader
from transformer.path import get_dictionary_path
from libcpp cimport bool
from libcpp.vector cimport vector
from libcpp.string cimport string
from cpython.version cimport PY_MAJOR_VERSION

print(PY_MAJOR_VERSION)

words = DictionaryLoader(get_dictionary_path()).words
lower_words = set([word.lower() for word in words])

cdef text_lower(word):
    return word.lower()

text_lower_ = text_lower
cdef text_isdigit(word):
    return word.isdigit()

cdef str text_isallcap(word):
    for letter in word:
        if not letter.istitle():
            return 'False'
    return 'True'

cdef text_istitle(word):
    if len(word) == 0:
        return 'False'
    try:
        titles = [s[0] for s in word.split(" ")]
        for token in titles:
            if token[0].istitle() is False:
                return 'False'
        return 'True'
    except:
        return 'False'

cdef str text_is_in_dict(word):
    return str(word.lower() in lower_words)

cdef str apply_function(name, word):
    functions = {
        "lower": text_lower,
        "istitle": text_istitle,
        "isallcap": text_isallcap,
        "isdigit": text_isdigit,
        "is_in_dict": text_is_in_dict
    }
    return str(functions[name](word))

cdef str template2features(list sent, list columns, int size, int i,
                           str token_syntax,
                           int column, int index1,
                           int index2, bool has_index2,
                           str func, bool has_func,
                           int debug=1):
    """
    :type token: object
    """
    cdef str prefix
    if debug:
        prefix = token_syntax + "="
    else:
        prefix = ""
    if i + index1 < 0:
        return prefix + "BOS"
    if i + index1 >= size:
        return prefix + "EOS"
    if has_index2:
        if i + index2 >= size:
            return prefix + "EOS"
        word = " ".join(columns[column][i + index1: i + index2 + 1])
    else:
        word = sent[i + index1][column]
    if has_func:
        result = apply_function(func, word)
    else:
        result = word
    return prefix + result



cdef list word2features(list sent, int i, list template):
    cdef list features = []
    cdef int x = 0
    cdef str output
    cdef list columns = []

    cdef int column
    cdef int index1
    cdef int index2
    cdef bool has_index2
    cdef str token_syntax
    cdef bool has_func
    cdef str func
    cdef str word

    for j in range(len(sent[0])):
        has_index2 = False
        has_func = False
        index = 0
        index2 = 0
        columns.append([t[j] for t in sent])
    cdef int size = len(sent)
    for token_syntax in template:
        matched = re.match(
            "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<function>.*))?", token_syntax)
        match_column = matched.group("column")
        if match_column:
            column = int(match_column)
        else:
            column = 0
        index1 = int(matched.group("index1"))
        match_index2 = matched.group("index2")
        if match_index2:
            has_index2 = True
            index2 = int(match_index2)
        match_func = matched.group("function")
        if match_func:
            has_func = True
            func = match_func
        output = template2features(sent, columns, size, i,
                                   token_syntax,
                                   column, index1,
                                   index2, has_index2,
                                   func, has_func)
        features.append(output)
    return features

cdef class FeatureTemplate:
    cdef int column
    cdef int index1
    cdef int index2
    cdef str token_syntax


cdef class TaggedTransformer:
    cdef list features
    cdef FeatureTemplate* features2

    def __init__(self, features=None):
        self.features = features

    def transform(self, sentences):
        X = [self.sentence2features(s) for s in sentences]
        y = [self.sentence2labels(s) for s in sentences]
        return X, y

    cdef list sentence2features(self, list s):
        cdef list tmp
        cdef list output = []
        cdef int l = len(s)
        for i in range(l):
            tmp = word2features(s, i, self.features)
            output.append(tmp)
        return output

    def sentence2labels(self, s):
        return [row[-1] for row in s]
