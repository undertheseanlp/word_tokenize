# -*- coding: utf-8 -*-
import pycrfsuite

from transformer import sent2labels
from transformer import Transformer

if __name__ == '__main__':
    transformer = Transformer()
    train_sents = transformer.load_train_sents()
    matrix = []
    for sentence in train_sents:
        matrix.append(transformer.list_to_tuple(transformer.format_word(sentence)))
    train_sents = matrix
    X_train = [Transformer.extract_features(s) for s in train_sents]
    y_train = [sent2labels(s) for s in train_sents]
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X_train, y_train):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })
    trainer.train("crf-model-1")
