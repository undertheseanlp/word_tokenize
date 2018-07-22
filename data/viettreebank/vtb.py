import os
from six.moves import cPickle
import nltk
import random
from io import open
from pyvltk import conf

CONF = conf.CONF

SENTENCES_PATH = os.path.join(CONF['corpus']['vtb_dir'], 'sentences.pickle')

LEN_VTB_SENTENCES = 10401

E_SYMBOL = ['*E*', '*T*', '*T*-1']


def read_vtb(filepath):
    with open(filepath, 'r', encoding='utf-8') as fi:
        for line in fi:
            line = line.strip()
            yield nltk.Tree.fromstring(line)


def convert_postag(pos):
    # if pos == '-':
    #     return pos
    if len(pos) >= 3:
        return pos.split('-')[0]
    else:
        return pos


def tree2data():
    trees = read_vtb(CONF['corpus']['vtb_file'])

    if os.path.isfile(SENTENCES_PATH):
        print("Load pickle from {}".format(SENTENCES_PATH))
        with open(SENTENCES_PATH, 'rb') as fi:
            sentences = cPickle.load(fi)
    else:
        with open(os.path.join(CONF['corpus']['vtb_dir'], 'vtb.pos'), 'w', encoding='utf-8') as fo:
            sentences = []
            for tree in trees:
                sentence = []
                for subtree in tree.subtrees(lambda t: t.height() == 2):
                    pos = subtree.label()
                    pos = convert_postag(pos)

                    # CHECK pos
                    # if pos != new_pos:
                    #     print(pos, new_pos, sep='\t')

                    word = subtree[0]
                    # print(word, pos, sep='\t')

                    # CHECK word
                    # if not word.isalpha():
                    #     if '_' in word:
                    #         sub_words = word.split('_')
                    #         for s_word in sub_words:
                    #             if not s_word.isalpha():
                    #                 print(word)
                    #                 break
                    #     else:
                    #         print(word)
                    if word in E_SYMBOL:
                        continue
                    fo.write(u"{}\t{}\n".format(word, pos))

                    sentence.append((word, pos))
                sentences.append(sentence)
                fo.write(u"\n")
            assert len(sentences) == LEN_VTB_SENTENCES
        random.shuffle(sentences)
        print("Write pickle to {}".format(SENTENCES_PATH))
        with open(SENTENCES_PATH, 'wb') as fi:
            cPickle.dump(sentences, fi, protocol=2)

    return sentences


def print_pos_tag(sentences=None):
    sentences = sentences or tree2data()
    vtb_ramdom_path = os.path.join(CONF['corpus']['vtb_dir'], 'vtb_random.pos')
    if not os.path.isfile(vtb_ramdom_path):
        print("Write to {}".format(vtb_ramdom_path))
        with open(vtb_ramdom_path, 'w', encoding='utf-8') as fo:
            for sentence in sentences:
                for word, pos in sentence:
                    fo.write(u"{}\t{}\n".format(word, pos))
                fo.write(u"\n")
                # return sentences


def print_tokenizer(sentences=None):
    sentences = sentences or tree2data()
    vtb_tokenizer_path = os.path.join(CONF['corpus']['vtb_dir'], 'vtb.tokenizer')

    if not os.path.isfile(vtb_tokenizer_path):
        tokenizer_sentences = get_tokenizer(sentences)
        print("Write to {}".format(vtb_tokenizer_path))
        with open(vtb_tokenizer_path, 'w', encoding='utf-8') as fo:
            for sentence in tokenizer_sentences:
                for word, tag in sentence:
                    fo.write(u"{}\t{}\n".format(word, tag))
                fo.write(u"\n")


def get_tokenizer(sentences=None):
    """

    :param sentences:
    :return:
    """
    sentences = sentences or tree2data()
    tokenizer_sentences = []
    for sentence in sentences:
        tokenizer_sentence = []
        for word, _ in sentence:
            ws = word.split('_')
            if len(ws) == 0:
                raise ValueError('Len ws == 0')
            tag = u'B'
            for w in ws:
                tokenizer_sentence.append([w, tag])
                tag = u'I'
        tokenizer_sentences.append(tokenizer_sentence)

    assert len(tokenizer_sentences) == LEN_VTB_SENTENCES
    return tokenizer_sentences


def get_postag(sentences=None):
    sentences = sentences or tree2data()
    return sentences


if __name__ == '__main__':
    # sentences = tree2data()
    # print_pos_tag()
    get_postag()