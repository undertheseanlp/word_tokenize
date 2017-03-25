# -*- coding: utf-8 -*-
punctuation = open("punctuation.txt", "r").read().splitlines()
punctuation = [unicode(charactor) for charactor in punctuation]


def compound_words(token):
    token = token.split('_')
    first_token = [(token[0], "BW")]
    last_token = [(i, "IW") for i in token[1:]]
    return first_token + last_token


def single_word(token):
    if token in punctuation:
        return [(token, 'O')]
    else:
        return [(token, 'BW')]


def tagged_token(token):
    if '_' in token:
        return compound_words(token)
    else:
        return single_word(token)


def to_column(sentence):
    tokens = [token for token in sentence.split()]
    tokens_tagged = [tagged_token(token) for token in tokens]
    tokens_tagged = [token_tagged for token_tagged in tokens_tagged]
    return tokens_tagged
