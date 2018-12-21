from underthesea.word_tokenize import tokenize
from .model import CRFModel


def word_tokenize(sentence, format=None, model_path=None):
    tokens = tokenize(sentence).split()
    model = CRFModel.instance(model_path)
    output = model.predict(tokens)
    tokens = [token[0] for token in output]
    tags = [token[1] for token in output]
    output = []
    for tag, token in zip(tags, tokens):
        if tag == "I-W":
            output[-1] = output[-1] + " " + token
        else:
            output.append(token)
    if format == "text":
        output = u" ".join([item.replace(" ", "_") for item in output])
    return output


if __name__ == '__main__':
    output = word_tokenize("Đang họp báo vụ điểm cao bất thường ở Sơn La", format="text")
    print(output)
