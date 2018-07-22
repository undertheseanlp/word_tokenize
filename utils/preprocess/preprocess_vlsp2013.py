from os.path import join
from languageflow.reader.tagged_corpus import TaggedCorpus
from utils.helpers import read, flat_list
import re


class Vlsp2013Preprocessor():

    RAW_PATH = 'data/vlsp2013/raw/combine/'
    CORPUS_PATH = 'data/vlsp2013/corpus/'

    def clean_sentences(self, file_name):
        content = read(file_name).split('\n')
        sents = [self._remove_postag(sent) for sent in content]
        sents = [sent for sent in sents if sent != '']
        return sents

    def preprocess(self, sentences):
        return [flat_list(self._process_sentence(sent)) for sent in sentences]

    def convert_raw_to_corpus(self):

        for file in ['train.txt', 'test.txt']:
            input_data = join(self.RAW_PATH, file)
            tagged_corpus = TaggedCorpus()
            sentences = self.clean_sentences(input_data)
            tagged_corpus.sentences = self.preprocess(sentences)

            output_data = join(self.CORPUS_PATH, file)
            tagged_corpus.save(output_data)

    def _remove_postag(self, sent):
        return re.sub('\/[A-Za-z]+', '', sent)

    def _process_token(self, token):
        return [[t, 'B-W'] if i == 0 else [t, 'I-W'] for i, t in enumerate(token)]

    def _process_sentence(self, sent):
        return [self._process_token(token.split('_')) for token in sent.split()]
