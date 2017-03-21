from string import ascii_lowercase, ascii_uppercase

from underthesea.corpus import PlainTextCorpus


class Pre_Process:
    @staticmethod
    def find_punctuation(folder, file_name):
        f_write = open(file_name, "w")
        punctuations = []
        corpus = PlainTextCorpus()
        corpus.load(folder)
        punctuations = sorted(punctuations)
        for punctuation in punctuations:
            f_write.write(punctuation.encode("utf-8") + "\n")
        return punctuations
