# -*- coding: utf-8 -*-
from underthesea.corpus import PlainTextCorpus
from os.path import dirname, join
from labs.compare_sentence.script import compare_sentence
from labs.computeF1.to_column import to_column

model_name = "output_crf"
output_folder = join(dirname(dirname(__file__)), "data", "corpus_2", "train", "output")
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus_2", "train", model_name)
print 0


def get_len(sentences):
    count = 0
    for x in sentences.split(" "):
        count += 1
    return count


def get_sentences(corpus):
    sentences = []
    for document in corpus.documents:
        sentences += document.sentences
    return sentences


expected_corpus = PlainTextCorpus()
expected_corpus.load(output_folder)
actual_corpus = PlainTextCorpus()
actual_corpus.load(model_output_folder)
total = 0
for sentence in get_sentences(expected_corpus):
    total += 1

correct = 0

f = open(join(dirname(__file__), "logs", "crf", "result.txt"), "w")
f1 = open(join(dirname(__file__), "logs", "crf", "result1.txt"), "w")
total_tokens = 0
score_per_sentence = 0
store_result_fail = []
actual_tokens = []
predict_tokens = []
predict = []
actual = []
log = []
fail_BW = 0
fail_IW = 0
for e, a in zip(expected_corpus.documents, actual_corpus.documents):
    for i, j in zip(e.sentences, a.sentences[:-1]):
        if i != j:
            print i + "\n" + j + "\n" + "\n"
            f.write(i.encode('utf-8') + "\n" + j.encode("utf-8") + "\n" + "\n")
            f1.write(i.encode('utf-8') + "\n" + j.encode("utf-8") + "\n" + "\n")
        result = compare_sentence(i, j)
        score_per_sentence += result["score"] * float(get_len(i))
        # total_tokens += get_len(j)
        if result['fail']:
            store_result_fail.append(result["fail"])
        for fail in result["fail"]:
            print fail[0]
            print fail[1]
            f.write(fail[0].encode("utf-8") + "\n" + fail[1].encode("utf-8") + "\n" + "\n")
            print ""

actual_column = []
predict_column = []
for e, a in zip(expected_corpus.documents, actual_corpus.documents):
    for i, j in zip(e.sentences, a.sentences[:-1]):
        predict_column.append(to_column(i))
        actual_column.append(to_column(j))

precision = float(score_per_sentence) / float(total_tokens + fail_BW)
recall = float(score_per_sentence) / float(total_tokens + fail_IW)
F = 2 * precision * recall / (precision + recall)
score = score_per_sentence * 100.0 / total_tokens
print ("recall :%0.2f percent" % (recall * 100))
print("Accuracy: %.2f percent" % score)
print("F1 = %0.2f percent" % (F * 100))
f.write("accuracy: " + str(score))
