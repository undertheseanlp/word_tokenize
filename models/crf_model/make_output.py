from underthesea.corpus import PlainTextCorpus
from os.path import join, dirname
from model import CRFModel
from transformer import Transformer
import time

start = time.time()
input_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
output_crf_folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "output_crf")
corpus = PlainTextCorpus()
corpus.load(input_folder)
output = PlainTextCorpus()
model = CRFModel()
for document in corpus.documents:
    print document.id
    sentences = document.sentences
    output = []
    for sentence in sentences:
        sentence = model.predict(sentence)
        output.append(sentence)
        # print 0

    document.sentences = output

count = 0
for document in corpus.documents:
    sentences = document.sentences
    count += sentences.__len__()
corpus.save(output_crf_folder)
stop = time.time()
time = stop - start
time_per_doc = time / count
print "speed time per doc " + str(time_per_doc)
