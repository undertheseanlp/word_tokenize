from os.path import dirname
from os.path import join

from underthesea.corpus import PlainTextCorpus

# pre-process

from models.crf_model.transformer import Transformer

punctuation = open("punctuation.txt", "r").read().split('\n')


# to sentence





def count_underscore(word):
    count = 0
    for token in word.split('_'):
        count += 1
    return count


def documents_to_sentences(documents):
    result_sentence = []
    for document in documents:
        for sentence in document.sentences:
            result_sentence.append(sentence)
    return result_sentence


def sent2vec(sentence):
    vector = []
    words = []
    for word in sentence.split(' '):
        if "_" in word:
            for i in range(count_underscore(word) - 1):
                vector.append(1)
                words.append(word)
        vector.append(0)
        words.append(word)
    return vector, words


transformer = Transformer()
train_sents = transformer.load_train_sents()
corpus = PlainTextCorpus()
folder = join(dirname(dirname(dirname(__file__))), "data", "raw", "train", "output")
corpus.load(folder)
total_sentences = documents_to_sentences(corpus.documents)
total_vec = []
vector = []
total_vector = []
total_words = []
for sentence in total_sentences[:-2]:
    total_vec.append(sent2vec(sentence))
for sentence in total_sentences[:-2]:
    words = []
    for word in sentence.split(' '):
        if '_' in word:
            for x in word.split('_'):
                words.append(x)
        words.append(word)
    total_words.append(words)

print 0
