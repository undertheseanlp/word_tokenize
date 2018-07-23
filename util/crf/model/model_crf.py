from os.path import join, dirname
import pycrfsuite
from underthesea.word_tokenize import tokenize

from util.crf.transformer.custom_transformer import CustomTransformer

path = join(dirname(__file__), "model.bin")
estimator = pycrfsuite.Tagger()
estimator.open(path)

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

def predict(sentence):
    sentence = tokenize(sentence).split()
    tokens = [(token, "X") for token in sentence]
    x = transformer.transform([tokens])[0][0]
    tags = estimator.tag(x)
    return list(zip(sentence, tags))

if __name__ == '__main__':
    y = predict("Tổng thống Nga coi việc Mỹ không kích căn cứ quân sự của Syria là sự gây hấn nhằm vào một quốc gia có chủ quyền")
    print(y)
