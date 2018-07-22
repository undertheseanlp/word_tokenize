import glob
from utils.preprocess import Vlsp2013Preprocessor, Vlsp2016Preprocessor
from utils.file_io.concat import concat_text_files
from src.train.transform import DataTransformer


def convert_raw_to_corpus():
    Vlsp2013Preprocessor().convert_raw_to_corpus()
    Vlsp2016Preprocessor().convert_raw_to_corpus()


def combine():
    io_paths = [{'inputs': glob.glob('data/vlsp2013/raw/Testset-POS/*.pos'),
                 'output': 'data/vlsp2013/raw/combine/test.txt'},

                {'inputs': glob.glob('data/vlsp2013/raw/Trainset-POS-full/*.pos'),
                 'output': 'data/vlsp2013/raw/combine/test.txt'},

                {'inputs': glob.glob('data/vlsp2013/raw/Trainset-POS-full/*.pos'),
                 'output': 'data/vlsp2013/raw/combine/train.txt'},

                {'inputs': ['data/vlsp2013/corpus/test.txt', 'data/vlsp2016/corpus/test.txt'],
                 'output': 'tmp/merge/test.txt'}]
    for path in io_paths:
        concat_text_files(**path)


def transform():
    DataTransformer(corpus_path='tmp/merge/{}.txt', save_path='tmp/cleaned/').execute()
