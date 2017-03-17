from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join

input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
corpus = PlainTextCorpus()
corpus.load(input_folder)
corpus.save("test_saved_corpus")
