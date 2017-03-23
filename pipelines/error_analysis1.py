from os.path import join, dirname

from underthesea.corpus import PlainTextCorpus


f1 = open(join(dirname(__file__), "logs", "crf", "fail_BW.txt"), "w")
f2 = open(join(dirname(__file__), "logs", "crf", "fail_IW.txt"), "w")
f3 = open(join(dirname(__file__), "logs", "crf", "fail_O.txt"), "w")
model_name = "output_crf"
output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", "output")
model_output_folder = join(dirname(dirname(__file__)), "data", "corpus", "train", model_name)
expected_corpus = PlainTextCorpus()
expected_corpus.load(output_folder)
actual_corpus = PlainTextCorpus()
actual_corpus.load(model_output_folder)
f1 = open(join(dirname(__file__), "logs", "crf", "fail_BW.txt"), "w")
f2 = open(join(dirname(__file__), "logs", "crf", "fail_IW.txt"), "w")
f3 = open(join(dirname(__file__), "logs", "crf", "fail_O.txt"), "w")


def to_column(sentence):
    words = []
    result = []
    path = join(dirname(dirname(dirname(__file__))), "pipelines", "logs", "punctuation.txt")
    punctuations = open(path, "r").read().split("\n")
    for punctuation in punctuations:
        punctuation = unicode(punctuations)
    for word in sentence.split(" "):
        words.append(word)
    if words[0] == "":
        words.pop(0)
    for word in words:
        tokens = []
        if word in punctuations:
            result.append((word, "O"))
        else:
            for token in word.split("_"):
                tokens.append(token)
            for i in range(len(tokens)):
                if i == 0:
                    if tokens[i] != "":
                        result.append((tokens[i], "BW"))
                else:
                    result.append((tokens[i], "IW"))
    return result

def compare_sentence_1(sentence_1, sentence_2):
    result = []
    sentence_1 = to_column(sentence_1)
    sentence_2 = to_column(sentence_2)
    # fail = [x for x in sentence_2 if x not in sentence_1]
    for x in range(len(sentence_2)):
        if sentence_2[x] != sentence_1[x]:
            result.append((sentence_2[x][0], sentence_2[x][1], sentence_1[x][0], sentence_1[x][1]))

    return result


for e, a in zip(expected_corpus.documents, actual_corpus.documents):
    for i, j in zip(e.sentences, a.sentences[:-1]):
        if i != j:
            total_fail = compare_sentence_1(i, j)
            BW = []
            IW = []
            O = []
            for x in total_fail:
                if x[1] == "BW":
                    BW.append(x)
                if x[1] == "IW":
                    IW.append(x)
                if x[1] == "O":
                    O.append(x)
            if len(BW) != 0:
                f1.write(i.encode('utf-8') + "\n" + j.encode('utf-8') + "\n \n")
                for a in BW:
                    if a[1] == "BW" and a[3] == "IW":
                        f1.write("%s(IW) -> %s(BW) \n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                    if a[1] == "BW" and a[3] == "O":
                        f1.write("%s(O) -> %s(BW) \n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                f1.write("\n")
                f1.write("=====================\n\n")
            if len(IW) != 0:
                f2.write(i.encode('utf-8') + "\n" + j.encode('utf-8') + "\n \n")
                for a in IW:
                    if a[1] == "IW" and a[3] == "BW":
                        f2.write("%s(BW) -> %s(IW) \n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                    if a[1] == "IW" and a[3] == "O":
                        f2.write("%s(O) -> %s(IW) \n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                f2.write("\n")
                f2.write("=====================\n\n")
            if len(O) != 0:
                f3.write(i.encode('utf-8') + "\n" + j.encode('utf-8') + "\n \n")
                for a in O:
                    if a[1] == "O" and a[3] == "BW":
                        f3.write("%s(BW) -> %s(O)\n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                    if a[1] == "O" and a[3] == "IW":
                        f3.write("%s(IW) -> %s(O)\n" % (a[0].encode('utf-8'), a[2].encode('utf-8')))
                f3.write("\n")
                f3.write("=====================\n\n")
