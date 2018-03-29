from os.path import join, dirname

from load_data import load_dataset
from custom_transformer import CustomTransformer
from feature_template import template
from model import CRFModel


if __name__ == '__main__':
    sentences = []
    for f in ["train.txt", "dev.txt"]:
        file = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016",
                    "corpus", f)
        sentences += load_dataset(file)

    transformer = CustomTransformer(template)
    model = CRFModel(transformer)
    model.transform(sentences)
    model.train()
    model.export()
