from os.path import join, dirname

from tools import readers


# PATH = '../../corpus/vlsp2016/{}.txt'
PATH = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", "{}.txt")


def get_tokenizer(fileids=('train', 'dev', 'test')):
    """
    :return: train_set, dev_set, test_set
    """
    len_fields = 2
    sep = '\t'

    out_data = []

    if 'train' in fileids:
        train_set = [sen for sen in readers.iob_reader(PATH.format('train'), len_fields, sep=sep)]
        out_data.append(train_set)

    if 'dev' in fileids:
        dev_set = [sen for sen in readers.iob_reader(PATH.format('dev'), len_fields, sep=sep)]
        out_data.append(dev_set)

    if 'test' in fileids:
        test_set = [sen for sen in readers.iob_reader(PATH.format('test'), len_fields, sep=sep)]
        out_data.append(test_set)

    return out_data
