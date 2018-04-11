from io import open


from feature_engineering.features import is_number, contain_digit, is_punct, contain_punct, get_pattern_for_word

BI_GRAMS = set()
TRI_GRAMS = set()

DICT_PATH = "words.txt"


with open(DICT_PATH, 'r', encoding='utf-8') as fin:
    for token in fin.read().split('\n'):
        tmp = token.split(' ')
        if len(tmp) == 2:
            BI_GRAMS.add(token)
        elif len(tmp) == 3:
            TRI_GRAMS.add(token)


def word2features(sent, i):
    word = sent[i]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        #   'word[-3:]': word[-3:],
        #   'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        # 'word.isdigit()': word.isdigit(),

        'word.isnumber': is_number(word),
        'word.contain_digit': contain_digit(word),
        'word.ispunct': is_punct(word),
        'word.contain_punct': contain_punct(word),
        'word.pattern': get_pattern_for_word(word)
    }
    if i > 0:
        word1 = sent[i - 1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:word.bi_gram()': ' '.join([word1, word]).lower() in BI_GRAMS,

            '-1:word.isnumber': is_number(word1),
            '-1:word.contain_digit': contain_digit(word),
            '-1:word.ispunct': is_punct(word),
            '-1:word.contain_punct': contain_punct(word),
            '-1:word.pattern': get_pattern_for_word(word)
        })
        if i > 1:
            word2 = sent[i - 2]
            features.update({
                '-2:word.tri_gram()': ' '.join([word2, word1, word]).lower() in TRI_GRAMS,
            })

        if i < len(sent) - 1:
            word_plus_1 = sent[i + 1]
            features.update({
                '-1|0|+1:word.tri_gram()': ' '.join([word1, word, word_plus_1]).lower() in TRI_GRAMS,
            })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:word.bi_gram()': ' '.join([word, word1]).lower() in BI_GRAMS,

            '+1:word.isnumber': is_number(word1),
            '+1:word.contain_digit': contain_digit(word),
            '+1:word.ispunct': is_punct(word),
            '+1:word.contain_punct': contain_punct(word),
            '+1:word.pattern': get_pattern_for_word(word)
        })
        if i < len(sent) - 2:
            word2 = sent[i + 2]
            features.update({
                '+2:word.tri_gram()': ' '.join([word, word1, word2]).lower() in TRI_GRAMS,
            })
    else:
        features['EOS'] = True

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, label in sent]


def sent2tokens(sent):
    return [token for token, label in sent]


if __name__ == '__main__':
    import json
    print(json.dumps(word2features(['a', 'b', 'c', 'd', 'e'], 2), indent=4))
