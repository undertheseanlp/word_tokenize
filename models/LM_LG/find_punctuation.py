from os.path import dirname
from os.path import join

from labs.computeF1.to_column import write_out_of_word


folder = join(dirname(dirname(dirname(__file__))), "data", "corpus", "train", "input")
file_name = "punctuation.txt"
write_out_of_word(folder, file_name)

