import shutil
from random import shuffle
from os.path import dirname, join
from os import listdir
path = join(dirname(dirname(dirname(__file__))), "data")
train_input = join(path, "corpus_2", "train", "input")
test_input = join(path, "corpus_2", "test", "input")
test_output = join(path, "corpus_2", "test", "output")
source_input = join(path, "raw", "train", "input")
source_output = join(path, "raw", "train", "output")
# ids_raw = listdir(source_input)
ids_seg = listdir(source_output)
shuffle(ids_seg)
# shuffle(ids_raw)
data_set = ids_seg[0:43]
input_test = ids_seg[44:48]
output_test = []
for file_name in data_set:
    shutil.copyfile(join(source_output, file_name), join(train_input, file_name))
for file_name in input_test:
    shutil.copyfile(join(source_output, file_name), join(test_output, file_name))
    file_name = file_name.replace(".seg", ".raw")
    shutil.copyfile(join(source_input, file_name), join(test_input, file_name))


