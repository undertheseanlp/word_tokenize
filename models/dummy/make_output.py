from underthesea.corpus import PlainTextCorpus
from os.path import join, dirname
from model import DummyModel

input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
output_dummy_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "output_dummy")
corpus = PlainTextCorpus()
corpus.load(input_folder)
output = PlainTextCorpus()
model = DummyModel()
for document in corpus.documents:
    sentences = document.sentences
    sentences = [sentence.lower() for sentence in sentences]
    output = [model.predict(s) for s in sentences]
    document.sentences = output
corpus.save(output_dummy_folder)
