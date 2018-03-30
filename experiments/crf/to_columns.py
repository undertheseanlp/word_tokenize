from os.path import join, dirname


def to_column(sentence):
    words = []
    result = []
    path = join(dirname(__file__), "punctuation.txt")
    with open(path, "r") as f:
        punctuations = f.read().split("\n")
    for word in sentence.split(" "):
        words.append(word)
    if words[0] == "":
        words.pop(0)
    for word in words:
        tokens = []
        if word in punctuations:
            result.append((word, "O"))
        else:
            for token in word.split("_"):
                tokens.append(token)
            for i in range(len(tokens)):
                if i == 0:
                    if tokens[i] != "":
                        result.append([tokens[i], "B-W"])
                else:
                    result.append([tokens[i], "I-W"])
    return result
