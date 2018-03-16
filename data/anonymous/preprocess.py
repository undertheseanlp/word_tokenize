import shutil
from random import shuffle
from os.path import dirname, join
from os import listdir, mkdir


if __name__ == '__main__':
    raw_input = join(dirname(__file__),  "raw", "input")
    raw_output = join(dirname(__file__), "raw", "output")
    docs = listdir(raw_output)
    shuffle(docs)
    train_docs = docs[0:43]
    test_docs = docs[44:48]

    output_test = []

    corpus_folder = join(dirname(__file__), "corpus")
    try:
        shutil.rmtree(corpus_folder)
    except:
        pass
    mkdir(corpus_folder)
    train_folder = join(corpus_folder, "train")
    test_folder = join(corpus_folder, "test")
    test_input = join(test_folder, "input")
    test_output = join(test_folder, "output")
    mkdir(train_folder)
    mkdir(test_folder)
    mkdir(test_input)
    mkdir(test_output)

    for file in train_docs:
        shutil.copyfile(join(raw_output, file), join(train_folder, file))

    for file in test_docs:
        shutil.copyfile(join(raw_output, file), join(test_output, file))
        file = file.replace(".seg", ".raw")
        shutil.copyfile(join(raw_input, file), join(test_input, file))


