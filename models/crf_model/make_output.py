# -*- coding: utf-8 -*-
from underthesea.corpus import PlainTextCorpus
from os.path import join, dirname

from labs.computeF1.to_column import write_out_of_word
from model import CRFModel
from transformer import Transformer
import time
from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join
from string import ascii_lowercase
from string import ascii_uppercase

start = time.time()
input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
output_crf_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "output_crf")
corpus = PlainTextCorpus()
corpus.load(input_folder)
output = PlainTextCorpus()
model = CRFModel()
for document in corpus.documents:
    print document.id
    sentences = document.sentences
    output = []
    for sentence in sentences:
        sentence = model.predict(sentence)
        output.append(sentence)
        # print 0

    document.sentences = output

count = 0
for document in corpus.documents:
    sentences = document.sentences
    count += sentences.__len__()
path = join(dirname(dirname(dirname(__file__))), 'data', 'raw', 'train', 'output')
file_name = join(dirname(dirname(dirname(__file__))), "pipelines", "logs", "punctuation.txt")

write_out_of_word(path, file_name)
corpus.save(output_crf_folder)
