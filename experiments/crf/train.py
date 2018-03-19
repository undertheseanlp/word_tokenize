from os.path import dirname, join

from custom_transformer import CustomTransformer
from load_data import load_dataset
from model import CRFModel

template = [
            "T[-2].lower", "T[-1].lower", "T[0].lower", "T[1].lower", "T[2].lower",
            "T[-1].isdigit", "T[0].isdigit", "T[1].isdigit",

            "T[-1].istitle", "T[0].istitle", "T[1].istitle",

            "T[0,1].istitle", "T[0,2].istitle",

            "T[-2].is_in_dict", "T[-1].is_in_dict", "T[0].is_in_dict", "T[1].is_in_dict", "T[2].is_in_dict",

            "T[-2,-1].is_in_dict", "T[-1,0].is_in_dict", "T[0,1].is_in_dict", "T[1,2].is_in_dict",

            "T[-2,0].is_in_dict", "T[-1,1].is_in_dict", "T[0,2].is_in_dict",

            # word unigram and bigram and trigram
            "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
            "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
            "T[-2,0]", "T[-1,1]", "T[0,2]",
            # BI tag
            "T[-2][1]", "T[-1][1]"
        ]
transformer = CustomTransformer(template)

if __name__ == '__main__':
    sentences = []
    for f in ["train.txt", "dev.txt", "test.txt"]:
        file = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus", f)
        sentences += load_dataset(file)
        # sentences = sentences[:1000]
    model = CRFModel(transformer)
    model.load_data(sentences)
    model.fit_transform()
    model.train()
    model.export()
