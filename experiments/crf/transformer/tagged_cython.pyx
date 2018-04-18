import re
from os.path import join, dirname

from cymem.cymem cimport Pool
from languageflow.reader.dictionary_loader import DictionaryLoader
from transformer.path import get_dictionary_path
from libcpp cimport bool
from libcpp.vector cimport vector
from libcpp.string cimport string

words = DictionaryLoader(get_dictionary_path()).words
lower_words = set([word.lower() for word in words])

cdef str text_lower(word):
    return word.lower()

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

cdef str template2features(list sent, list columns,
                        int size, int i,
                        FeatureTemplate feature,
                        int debug=1):
    """
    :type token: object
    """
    cdef str prefix
    cdef str token_syntax = feature.token_syntax.decode("utf-8")
    cdef str func = feature.func.decode("utf-8")
    if debug:
        prefix = token_syntax + "="
    else:
        prefix = ""
    if i + feature.index1 < 0:
        return prefix + "BOS"
    if i + feature.index1 >= size:
        return prefix + "EOS"

    if feature.has_index2:
        print("match index2")
        if i + feature.index2 >= size:
            return prefix + "EOS"
        word = " ".join(columns[feature.column][i + feature.index1: i + feature.index2 + 1])
    else:
        word = sent[i + feature.index1][feature.column]

    if feature.has_func:
        result = apply_function(func, word)
    else:
        result = word
    return prefix + result

cdef list word2features(list sent, int i,
                        FeatureTemplate*features,
                        int n_features):
    cdef str tmp
    cdef list output = []
    cdef list columns = []

    for j in range(len(sent[0])):
        columns.append([t[j] for t in sent])

    cdef int size = len(sent)

    for feature_index in range(n_features):
        tmp = template2features(sent, columns,
                                    size, i,
                                    features[feature_index])
        output.append(tmp)
    return output

cdef struct FeatureTemplate:
    int column
    int index1
    int index2
    string func
    string token_syntax
    bool has_column
    bool has_index2
    bool has_func

cdef class TaggedTransformer:
    cdef Pool mem
    cdef FeatureTemplate*features
    cdef int n_features

    def __init__(self, features=None):
        cdef:
            int column = 0
            int index1 = 0
            int index2 = 0
            string func = b''
            str syntax
            string token_syntax = b''
            bool has_column = True
            bool has_index2 = True
            bool has_func = True
        n_features = len(features)
        self.n_features = n_features
        self.mem = Pool()
        self.features = <FeatureTemplate*> self.mem.alloc(n_features, sizeof(FeatureTemplate))
        for i in range(n_features):
            syntax = features[i]
            matched = re.match(
                "T\[(?P<index1>\-?\d+)(\,(?P<index2>\-?\d+))?\](\[(?P<column>.*)\])?(\.(?P<func>.*))?", syntax)
            token_syntax = syntax.encode("utf-8")
            match_column = matched.group("column")
            match_index1 = matched.group("index1")
            match_index2 = matched.group("index2")
            match_func = matched.group("func")
            if match_column:
                column = int(match_column)
            else:
                has_column = False
            index1 = int(match_index1)
            if match_index2:
                index2 = int(match_index2)
            else:
                has_index2 = False
            if match_func:
                func = match_func.encode("utf-8")
            else:
                has_func = False
            self.features[i].column = column
            self.features[i].index1 = index1
            self.features[i].index2 = index2
            self.features[i].func = func
            self.features[i].token_syntax = token_syntax
            self.features[i].has_column = has_column
            self.features[i].has_index2 = has_index2
            self.features[i].has_func = has_func

    def transform(self, sentences):
        X = [self.sentence2features(s) for s in sentences]
        y = [self.sentence2labels(s) for s in sentences]
        return X, y

    cdef list sentence2features(self, list s):
        cdef list tmp
        cdef list output = []
        cdef int l = len(s)
        for i in range(l):
            tmp = word2features(s, i, self.features, self.n_features)
            output.append(tmp)
        return output

    def sentence2labels(self, s):
        return [row[-1] for row in s]
