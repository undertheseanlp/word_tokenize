from utils.read_write.readers import iob_reader


class DataLoader():

    CORPUS_PATH = 'data/vlsp2016/corpus/{}.txt'

    def __init__(self):
        self.fileids = ['train', 'dev', 'test']
        self.len_fields = 2
        self.sep = '\t'

    def get_tokenizer():
        out_data = []
        for file in self.fileids:
            try:
                data = [sent for sent in iob_reader(self.CORPUS_PATH.format('train'),
                                                    self.len_fields,
                                                    self.sep)]
                out_data.append(data)
            except Exception as e:
                raise e
        return out_data
