from languageflow.transformer.tagged import TaggedTransformer


class Trainer:
    def __init__(self, tagger, corpus):
        self.tagger = tagger
        self.corpus = corpus

    def train(self, c1, c2, feature):
        transformer = TaggedTransformer(self.tagger.features)
        X_train, y_train = transformer.transform(self.corpus.train, contain_labels=True)
        pass