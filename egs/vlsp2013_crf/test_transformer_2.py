
import time

import languageflow.transformer.tagged as tagged

from data import DataReader
from transformer_2 import TaggedTransformer

start = time.time()
corpus = DataReader.load_tagged_corpus("/home/anhv/.languageflow/datasets/VLSP2013-WTK/",
                                       train_file="train.txt", test_file="test.txt")

print(time.time() - start)



sentences = corpus.train

features = [
    "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
    "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
    "T[-2,0]", "T[-1,1]", "T[0,2]",

    "T[-2].lower", "T[-1].lower", "T[0].lower", "T[1].lower", "T[2].lower",
    "T[-2,-1].lower", "T[-1,0].lower", "T[0,1].lower", "T[1,2].lower",

    "T[-1].isdigit", "T[0].isdigit", "T[1].isdigit",

    "T[-2].istitle", "T[-1].istitle", "T[0].istitle", "T[1].istitle", "T[2].istitle",
    "T[0,1].istitle", "T[0,2].istitle",

    "T[-2].is_in_dict", "T[-1].is_in_dict", "T[0].is_in_dict", "T[1].is_in_dict", "T[2].is_in_dict",
    "T[-2,-1].is_in_dict", "T[-1,0].is_in_dict", "T[0,1].is_in_dict", "T[1,2].is_in_dict",
    "T[-2,0].is_in_dict", "T[-1,1].is_in_dict", "T[0,2].is_in_dict",
]

start = time.time()
transformer = TaggedTransformer(features)
vectors = transformer.transform(sentences, contain_labels=True)
print(time.time() - start)

start = time.time()
transformer_2 = tagged.TaggedTransformer(features)
vectors2 = transformer_2.transform(sentences, contain_labels=True)
print(time.time() - start)