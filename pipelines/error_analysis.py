from os.path import dirname
from os.path import join
from underthesea.corpus import PlainTextCorpus

model_name = "output_crf"
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", model_name)
input_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "input")
actual_corpus = PlainTextCorpus()
actual_corpus.load(model_output_folder)
input_corpus = PlainTextCorpus()
input_corpus.load(input_folder)

f = open(join(dirname(__file__), "error_analysis", "input_word.txt"), "w")
f1 = open(join(dirname(__file__), "error_analysis", "output_word.txt"), "w")
actual_words = []
input_words = []
for a in actual_corpus.documents:
    for a_sentences in a.sentences:
        for a_word in a_sentences.split(' '):
            actual_words.append(a_word)
for i in input_corpus.documents:
    for i_sentences in i.sentences:
        for i_word in i_sentences.split(' '):
            input_words.append(i_word)
for word in input_words:
    if word not in actual_words:
        f.write(word.encode('utf-8') + "\n")
for word in actual_words:
    if word not in actual_words:
        f1.write(word.encode('utf-8') + "\n")
print 0
