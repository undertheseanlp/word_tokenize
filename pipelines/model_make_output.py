from os.path import join, dirname
from pipelines import model_name
import importlib

if __name__ == '__main__':
    input_folder = join((dirname(dirname(__file__))), "data", "corpus", "test", "input")
    output_folder = join((dirname(dirname(__file__))), "data", "corpus", "test", "output_" + model_name)
    make_output = importlib.import_module("models.%s.make_output" % model_name).make_output
    make_output(input_folder, output_folder)