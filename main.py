import glob
from utils.preprocess.preprocess_vlsp2016 import Vlsp2016Preprocessor
from utils.preprocess.preprocess_vlsp2013 import Vlsp2013Preprocessor
from src.transform import DataTransformer
from src.train import CRFWrapper
from utils.preprocess.preprocess_vlsp2013 import Vlsp2013Combiner

if __name__ == '__main__':
    # Vlsp2016Preprocessor().convert_raw_to_corpus()
    # DataTransformer().execute()
    # Vlsp2013Combiner(
    #     inputs=glob.glob('data/vlsp2013/raw/Testset-POS/*.pos'),
    #     output='data/vlsp2013/raw/combine/test.txt'
    # ).combine()

    # Vlsp2013Combiner(
    #     inputs=glob.glob('data/vlsp2013/raw/Trainset-POS-full/*.pos'),
    #     output='data/vlsp2013/raw/combine/train.txt'
    # ).combine()

    Vlsp2013Preprocessor().convert_raw_to_corpus()
