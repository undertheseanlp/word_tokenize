import os

import pycrfsuite
from languageflow.transformer.tagged import TaggedTransformer
import logging

from conlleval import evaluate_

logger = logging.getLogger(__name__)
logger.setLevel(10)
FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT)


class Trainer:
    def __init__(self, tagger, corpus):
        self.tagger = tagger
        self.corpus = corpus

    def train(self, c1, c2, feature):
        transformer = TaggedTransformer(self.tagger.features)
        logger.info("Start feature extraction")
        X_train, y_train = transformer.transform(self.corpus.train, contain_labels=True)
        X_test, y_test = transformer.transform(self.corpus.test, contain_labels=True)
        logger.info("Finish feature extraction")

        # Train
        logger.info("Start train")
        params = {
            'c1': 1.0,  # coefficient for L1 penalty
            'c2': 1e-3,  # coefficient for L2 penalty
            'max_iterations': 200,  #
            # include transitions that are possible, but not observed
            'feature.possible_transitions': True
        }
        trainer = pycrfsuite.Trainer(verbose=True)
        for xseq, yseq in zip(X_train, y_train):
            trainer.append(xseq, yseq)
        trainer.set_params(params)
        filename = 'tmp/model.tmp'
        trainer.train(filename)
        logger.info("Finish train")

        # Tagger
        logger.info("Start tagger")
        tagger = pycrfsuite.Tagger()
        tagger.open(filename)
        y_pred = [tagger.tag(xseq) for x_seq in X_test]
        sentences = [[item[0] for item in sentence] for sentence in self.corpus.test]
        sentences = zip(sentences, y_test, y_pred)
        texts = []
        for s in sentences:
            tokens, y_true, y_pred = s
            tokens_ = ["\t".join(item) for item in zip(tokens, y_true, y_pred)]
            text = "\n".join(tokens_)
            texts.append(text)
        text = "\n\n".join(texts)
        open("tmp/output.txt", "w").write(text)
        evaluate_("tmp/output.txt")
        logger.info("Finish tagger")
