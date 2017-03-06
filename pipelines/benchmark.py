from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join

output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output")
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output_dummy")


def get_sentences(corpus):
    sentences = []
    for document in corpus.documents:
        sentences += document.sentences
    return sentences


expected_corpus = PlainTextCorpus()
expected_corpus.load(output_folder)
actual_corpus = PlainTextCorpus()
actual_corpus.load(model_output_folder)

total = len(get_sentences(expected_corpus))
correct = 0
for e, a in zip(expected_corpus.documents, actual_corpus.documents):
    expected_sentences = e.sentences
    actual_sentences = a.sentences[:-1]
    if len(expected_sentences) != len(actual_sentences):
        print e.id, len(e.sentences)
        print a.id, len(a.sentences)
    for i, j in zip(expected_sentences, actual_sentences):
        if i == j:
            correct += 1

score = correct * 100.0 / total
print("Accuracy: %.2f percent" % score)
