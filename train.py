import argparse
import os
from util.crf.train import train

parser = argparse.ArgumentParser("train.py")
parser.add_argument("--mode", help="available modes: train, train-test, train-test-split, cross-validation", default="train")
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--train-test-split", type=float,
                    help="train/test split ratio")
parser.add_argument("-s", help="path to save model")
parser.add_argument("--cross-validation", type=int, help="cross validation")

args = parser.parse_args()

if args.mode == "train":
    if not (args.train and args.s):
        parser.error("Mode train requires --train and -s")
    train_path = os.path.abspath(args.train)
    model_path = os.path.abspath(args.s)
    train(train_path=train_path, model_path=model_path)
    print("Model is saved in {}".format(model_path))