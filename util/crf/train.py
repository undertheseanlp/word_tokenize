import os
from os import makedirs
from os.path import dirname
from languageflow.model.crf import CRF
from languageflow.transformer.tagged import TaggedTransformer
from util.crf.conlleval import evaluate
from util.crf.word_tokenize import CRFModel
from .load_data import load_dataset

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
]


def train(train_path, model_path):
    train_set = []

    train_set += load_dataset(train_path)
    print("Load data from file", train_path)
    transformer = TaggedTransformer(template)
    X, y = transformer.transform(train_set, contain_labels=True)

    # train
    params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    folder = dirname(model_path)
    try:
        makedirs(folder)
    except:
        pass
    estimator = CRF(params=params, filename=model_path)
    estimator.fit(X, y)


def _remove_file(output_path):
    try:
        os.remove(output_path)
    except:
        pass


def train_test(train_path, test_path):
    model_path = "model.tmp.bin"
    output_path = "output.txt"
    _remove_file(output_path)
    output = open(output_path, "a")
    train(train_path, model_path)
    estimator = CRFModel.instance(model_path)

    test = load_dataset(test_path)
    for sample in test:
        sentence = [token[0] for token in sample]
        y_test = [token[1] for token in sample]
        y_pred = estimator.predict(sentence)
        for i in range(len(y_test)):
            line = "{}\t{}\t{}\n".format(y_pred[i][0], y_test[i], y_pred[i][1])
            output.write(line)
        output.write("\n")

    class Args(object):
        pass

    args = Args()
    args.latex = False
    args.raw = False
    args.delimiter = None
    args.oTag = "O"
    evaluate(open(output_path), args)

    os.remove(model_path)
    os.remove(output_path)
