from os.path import dirname, join
from underthesea_flow.flow import Flow
from underthesea_flow.model import Model
from underthesea_flow.model.crf import CRF
from underthesea_flow.transformer.tagged import TaggedTransformer
from underthesea_flow.validation.validation import TrainTestSplitValidation

from preprocess import vlsp2016

if __name__ == '__main__':
    # =========================================================================#
    # Start an experiment with flow
    # =========================================================================#
    flow = Flow()

    # =========================================================================#
    #                               Data
    # =========================================================================#

    # for evaluation
    # file = join(dirname(__file__), "corpus", "treebank", "train.txt")
    # sentences = treebank.load_data(file)

    # for saving model
    sentences = []
    for f in ["train.txt", "dev.txt", "test.txt"]:
        # for f in ["test.txt"]:
        file = join(dirname(__file__), "corpus", "vlsp2016", f)
        sentences += vlsp2016.load_data(file)

    flow.data(sentences=sentences)

    # =========================================================================#
    #                                Transformer
    # =========================================================================#
    template = [
        "T[-1].lower", "T[0].lower", "T[1].lower",
        "T[-1].isdigit", "T[0].isdigit", "T[1].isdigit",
        "T[-1].istitle", "T[0].istitle", "T[1].istitle",
        "T[0,1].istitle", "T[0,2].istitle",
        "T[-1].is_in_dict", "T[0].is_in_dict", "T[1].is_in_dict",
        "T[0,1].is_in_dict", "T[0,2].is_in_dict",
        # word unigram and bigram and trigram
        "T[-2]", "T[-1]", "T[0]", "T[1]", "T[2]",
        "T[-2,-1]", "T[-1,0]", "T[0,1]", "T[1,2]",
        "T[-2,0]", "T[-1,1]", "T[0,2]",
        # BI tag
        "T[-2][1]", "T[-1][1]"
    ]
    transformer = TaggedTransformer(template)

    flow.transform(transformer)

    # =========================================================================#
    #                               Models
    # =========================================================================#
    crf_params = {
        'c1': 1.0,  # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 1000,  #
        # include transitions that are possible, but not observed
        'feature.possible_transitions': True
    }
    flow.add_model(Model(CRF(params=crf_params), "CRF"))

    # =========================================================================#
    #                              Evaluation
    # =========================================================================#
    flow.add_score('f1_chunk')
    flow.add_score('accuracy_chunk')

    flow.set_validation(TrainTestSplitValidation(test_size=0.1))

    # =========================================================================#
    #                            Run Experiment
    # =========================================================================#

    flow.train()

    # flow.save_model("CRF", filename="wordsent_crf_7_20171009.model")
