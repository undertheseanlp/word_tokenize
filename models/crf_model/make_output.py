# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join
import time

from model import CRFModel
from underthesea.corpus import PlainTextCorpus

start = time.time()
input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "test", "input")
output_crf_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "test", "output_crf")
# input_folder = join(dirname(dirname(dirname(__file__))), "data", "test", "input")
# output_crf_folder = join(dirname(dirname(dirname(__file__))), "data", "test", "output")
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

    document.sentences = output

count = 0
for document in corpus.documents:
    sentences = document.sentences
    count += sentences.__len__()
# path = join(dirname(dirname(dirname(__file__))), 'data', 'raw', 'train', 'output')
# file_name = join(dirname(dirname(dirname(__file__))), "pipelines", "logs", "punctuation.txt")
# write_out_of_word(path, file_name)

corpus.save(output_crf_folder)
