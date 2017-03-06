from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join
import pandas as pd

print("[Stat] Train Data Set")
train_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "input")
train_corpus = PlainTextCorpus()
train_corpus.load(train_folder)
print("Total documents: %d" % len(train_corpus.documents))
s = pd.Series([len(d.sentences) for d in train_corpus.documents])
print("Sentences in documents")
print(pd.Series.describe(s))
print("Total sentences: %d" % sum(s))

print("\n")
print("[Stat] Test Data Set")
train_folder = join(dirname(dirname(__file__)), "data", "corpus", "test", "input")
test_corpus = PlainTextCorpus()
test_corpus.load(train_folder)
print("Total documents: %d" % len(test_corpus.documents))
s = pd.Series([len(d.sentences) for d in test_corpus.documents])
print("Sentences in documents")
print(pd.Series.describe(s))
print("Total sentences: %d" % sum(s))
