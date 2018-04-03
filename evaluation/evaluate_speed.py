"""
File output co dang nhu CONLL

Toi B-W I-W
la B-W B-W
...
...

"""
import sys
import argparse


def main(exp_path):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output_test", type=str, help="File output test")

    args = parser.parse_args()

    main(**vars(args))
