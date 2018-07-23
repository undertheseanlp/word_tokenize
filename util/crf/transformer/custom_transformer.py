from languageflow.transformer.tagged import TaggedTransformer
from languageflow.transformer.tagged_feature import word2features


class CustomTransformer(TaggedTransformer):
    def _convert_features_to_dict(self, features):
        return dict([k.split("=") for k in features])

    def _convert_features_to_list(self, features):
        return ["{}={}".format(k, v) for k, v in features.items()]
        pass

    def _word2features(self, s, i, template):
        features = word2features(s, i, template)
        features = self._convert_features_to_dict(features)
        return features

    def sentence2features(self, s):
        output = [self._word2features(s, i, self.template) for i in
                  range(len(s))]
        return output
