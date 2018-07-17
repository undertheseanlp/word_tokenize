from os import makedirs
from os.path import dirname, join, exists
from languageflow.reader.tagged_corpus import TaggedCorpus
import argparse


class VlspPreprocessor():

    RAW_PATH = 'data/vlsp2016/raw/'
    CORPUS_PATH = 'data/vlsp2016/corpus/'

    if not exists(CORPUS_PATH):
        makedirs(CORPUS_PATH)

    def __init__(self, file):
        self.file = file

    def load_data(self):
        tagged_corpus = TaggedCorpus()
        tagged_corpus.load(self.file)
        sentences = tagged_corpus.sentences
        return sentences

    def preprocess(self, sentences):
        return [self._process_sentence(sent) for sent in sentences]

    def convert_raw_to_corpus(self, output):

        for file in ['train.txt', 'dev.txt', 'test.txt']:
            input_data = join(self.RAW_PATH, f)
            tagged_corpus = TaggedCorpus()

            tagged_corpus.load(input_data)
            sentences = tagged_corpus.sentences
            tagged_corpus.sentences = self.preprocess(sentences)

            output_data = join(self.CORPUS_PATH, f)
            tagged_corpus.save(output_data)

    def _process_token(self, t):
        tokens = t[0].split('_')
        tokens = [token for i, token in enumerate(tokens)]
        output = [[token, 'B-W'] if i == 0 else [token, 'I-W'] for i, token in enumerate(tokens)]
        return output

    def _flat_list(self, nested_list):
        return [item for sublist in nested_list for item in sublist]

    def _process_sentence(sent):
        tokens = [self._process_token(token) for token in sent]
        output = self._flat_list(tokens)
        return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser('preprocess_vlsp2016.py')
    parser.add_argument('--sample', help='sample size', type=int)
    parser.add_argument('--output', help='output path')
    args = parser.parse_args()
    if args.sample:
        if not args.output:
            parser.error('You must set --output when use option --sample')
    raw_to_corpus(sample=args.sample, output=args.output)
