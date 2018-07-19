from os import makedirs
from os.path import join, exists
from languageflow.reader.tagged_corpus import TaggedCorpus
from utils.helpers import flat_list


class Vlsp2016Preprocessor():

    RAW_PATH = 'data/vlsp2016/raw/'
    CORPUS_PATH = 'data/vlsp2016/corpus/'

    if not exists(CORPUS_PATH):
        makedirs(CORPUS_PATH)

    def preprocess(self, sentences):
        return [self._process_sentence(sent) for sent in sentences]

    def convert_raw_to_corpus(self):

        for file in ['train.txt', 'dev.txt', 'test.txt']:
            input_data = join(self.RAW_PATH, file)
            tagged_corpus = TaggedCorpus()

            tagged_corpus.load(input_data)
            sentences = tagged_corpus.sentences
            tagged_corpus.sentences = self.preprocess(sentences)

            output_data = join(self.CORPUS_PATH, file)
            tagged_corpus.save(output_data)

    def _process_token(self, t):
        tokens = t[0].split('_')
        tokens = [token for i, token in enumerate(tokens)]
        output = [[token, 'B-W'] if i == 0 else [token, 'I-W'] for i, token in enumerate(tokens)]
        return output

    def _process_sentence(self, sent):
        tokens = [self._process_token(token) for token in sent]
        output = flat_list(tokens)
        return output



