# -*- coding: utf-8 -*-
from model import CRFModel
from underthesea.corpus import PlainTextCorpus


def make_output(input_folder, output_folder):
    corpus = PlainTextCorpus()
    corpus.load(input_folder)
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
    corpus.save(output_folder)
