from os.path import join, dirname
import time
from load_data import load_dataset
from feature_template import template
from transformer import tagged_cython
from transformer import tagged
import cProfile


def main():
    train_set = []
    for f in ["train.txt", "dev.txt"]:
        file = join(dirname(dirname(dirname(__file__))), "data", "vlsp2016",
                    "corpus", f)
        train_set += load_dataset(file)

    train_set = train_set[:100]

    start = time.time()
    transformer = tagged.TaggedTransformer(template)
    X1, y1 = transformer.transform(train_set)
    end = time.time()
    py = end - start
    # py = 2.34531

    start = time.time()
    transformer = tagged_cython.TaggedTransformer(template)
    X2, y2 = transformer.transform(train_set)
    end = time.time()
    cy = end - start

    print("Python:", py)
    print("Cython:", cy)
    print("Cython is {:0.3f}x faster ^-^".format(py / cy))
    # assert(X1 == X2)


if __name__ == '__main__':
    main()
