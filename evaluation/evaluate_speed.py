import sys
from os.path import dirname, join

current_folder = dirname(__file__)
# path = join(dirname(current_folder), "experiments", "abc")
path = "../experiments/abc"
print(path)
sys.path.append(path)

from final_model import f1
f1()