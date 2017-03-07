from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join

output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output")
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output_dictionary_11")


def vietnamese_lower(s):
    if type(s) == type(u""):
        return s.lower()
    return unicode(s, "utf8").lower().encode("utf8")


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
    new_expected_sentences = []
    for expected_sentence in expected_sentences:
        new_expected_sentences.append(vietnamese_lower(expected_sentence))
    actual_sentences = a.sentences[:-1]
    new_actual_sentences = []
    for actual_sentence in actual_sentences:
        new_actual_sentences.append(actual_sentence)

    expected_sentences = new_expected_sentences
    actual_sentences = new_actual_sentences
    if len(expected_sentences) != len(actual_sentences):
        print e.id, len(e.sentences)
        print a.id, len(a.sentences)
    for i, j in zip(expected_sentences, actual_sentences):
        if i == j:
            correct += 1
        else:
            print i
            print j

score = correct * 100.0 / total
print("Accuracy: %.2f percent" % score)
