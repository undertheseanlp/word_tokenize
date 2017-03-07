from underthesea.corpus import PlainTextCorpus
from os.path import join, dirname
from model import DictionaryModel

count = 0


def vietnamese_lower(s):
    if type(s) == type(u""):
        return s.lower()
    return unicode(s, "utf8").lower().encode("utf8")


input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
output_dummy_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "output_dictionary_11")
corpus = PlainTextCorpus()
corpus.load(input_folder)
output = PlainTextCorpus()
model = DictionaryModel()
for document in corpus.documents:
    print document.id
    sentences = document.sentences
    new_sentences = []
    for sentence in sentences:
        new_sentences.append(vietnamese_lower(sentence))
    sentences = new_sentences
    output = [model.predict(s) for s in sentences]
    document.sentences = output
corpus.save(output_dummy_folder)
