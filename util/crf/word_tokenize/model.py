from os.path import join, dirname
import pycrfsuite
from util.crf.transformer.custom_transformer import CustomTransformer
from util.crf.word_tokenize.features import template

transformer = CustomTransformer(template)


class CRFModel:
    objects = {}

    def __init__(self, model_path=None):
        if not model_path:
            model_path = join(dirname(__file__), "model.bin")
        estimator = pycrfsuite.Tagger()
        estimator.open(model_path)
        self.estimator = estimator

    @classmethod
    def instance(cls, model_path=None):
        if model_path not in cls.objects:
            cls.objects[model_path] = cls(model_path)
        object = cls.objects[model_path]
        return object

    def predict(self, sentence, format=None):
        tokens = [(token, "X") for token in sentence]
        x = transformer.transform([tokens])[0][0]
        tags = self.estimator.tag(x)
        return list(zip(sentence, tags))
