from os.path import dirname, join
from custom_transformer import CustomTransformer
from languageflow.flow import Flow
from languageflow.model import Model
from languageflow.model.crf import CRF
from languageflow.validation.validation import TrainTestSplitValidation
from load_data import load_dataset

if __name__ == '__main__':
    # =========================================================================#
    # Start an experiment with flow
    # =========================================================================#
    flow = Flow()
    flow.log_folder = "logs"

    # =========================================================================#
    #                               Data
    # =========================================================================#
    sentences = []
    for f in ["train.txt", "dev.txt", "test.txt"]:
        file = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016", "corpus",  f)
        sentences = sentences.append(load_dataset(file))
    flow.data(sentences=sentences)

    # =========================================================================#
    #                                Transformer
    # =========================================================================#
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

    # flow.save_model("CRF", filename="wordsent_crf_20180316.model")
