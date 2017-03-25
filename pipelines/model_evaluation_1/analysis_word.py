from os.path import dirname
from os.path import join

from underthesea.corpus import PlainTextCorpus
from underthesea.corpus import viet_dict_11K


def compare_dictionary(model_output_folder):
    # f = open(join(dirname(__file__), "logs", "crf", "new_word.txt"), "w")
    # f1 = open(join(dirname(__file__), "logs", "crf", "word_in_dictionary.txt"), "w")
    corpus = PlainTextCorpus()
    corpus.load(model_output_folder)
    new_words = []
    words = []
    for document in corpus.documents:
        for sentences in document.sentences:
            for word in sentences.split(" "):
                if '_' in word:
                    new_words.append(word)
    dictionary = viet_dict_11K.words
    for word in new_words:
        words.append(word.replace('_', ' '))
    new_word = [x for x in words if x not in dictionary]

    new_word = set(new_word)
    new_word = sorted(new_word)
    new_word_per_dict = float(len(new_word)) / float(len(dictionary)) * 100
    # f.write("Scale word not in dictionary %0.2f: \n" % new_word_per_dict)
    # for word in new_word:
    #     f.write(word.encode('utf-8') + "\n")
    word_in_dictionary = [x for x in words if x in dictionary]

    word_in_dictionary = set(word_in_dictionary)
    word_in_dictionary = sorted(word_in_dictionary)
    word_in_dictionary_per_total = float(len(word_in_dictionary)) / float(len(viet_dict_11K.words))
    # f1.write("scale word in dictionary: %0.2f \n" % word_in_dictionary_per_total)
    # for word in word_in_dictionary:
    #     f1.write(word.encode('utf-8') + "\n")
    return new_word, word_in_dictionary


if __name__ == '__main__':
    model_name = "output_crf"
    model_output_folder = join(dirname(dirname(__file__)), "data", "corpus_2", "test", model_name)
    (new_word, word_in_dictionary) = compare_dictionary(model_output_folder)
