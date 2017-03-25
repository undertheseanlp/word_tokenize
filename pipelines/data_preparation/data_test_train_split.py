import shutil
from random import shuffle
from os.path import dirname, join
from os import listdir

train_input = join(dirname(dirname(__file__)), "data", "corpus_2", "train", "input")
test_input = join(dirname(dirname(__file__)), "data", "corpus_2", "test", "input")
test_output = join(dirname(dirname(__file__)), "data", "corpus_2", "test", "output")
source_input = join(dirname(dirname(__file__)), "data", "raw", "train", "input")
source_output = join(dirname(dirname(__file__)), "data", "raw", "train", "output")
ids_raw = listdir(source_input)
ids_seg = listdir(source_output)
shuffle(ids_seg)
shuffle(ids_raw)
train = ids_seg[0:43]
input_test = ids_raw[44:48]
output_test = []
for file_name in train:
    shutil.copyfile(join(source_output, file_name), join(train_input, file_name))
for file_name in input_test:
    shutil.copyfile(join(source_input, file_name), join(test_input, file_name))
    output_test.append(file_name.replace(".raw", ".seg"))
for file_name in output_test:
    shutil.copyfile(join(source_output, file_name), join(test_output, file_name))

