import argparse
import os
from util.crf.train import train, train_test

parser = argparse.ArgumentParser("train.py")
parser.add_argument("mode", default="train", nargs="?",
  help="available modes: train, train-test, train-test-split, cross-validation")
parser.add_argument("--train", help="train folder")
parser.add_argument("--test", help="test folder")
parser.add_argument("--train-test-split", type=float,
                    help="train/test split ratio")
parser.add_argument("--model", help="path to save model")
parser.add_argument("--cross-validation", type=int, help="cross validation")

args = parser.parse_args()

mode = args.mode
if mode == "train":
    if not (args.train and args.model):
        parser.error("Mode train requires --train and --model")
    train_path = os.path.abspath(args.train)
    model_path = os.path.abspath(args.model)
    train(train_path=train_path, model_path=model_path)
    print("Model is saved in {}".format(model_path))

if mode == "train-test":
    if not (args.train and args.test):
        parser.error("Mode train-test requires --train and --test")
    train_path = os.path.abspath(args.train)
    test_path = os.path.abspath(args.test)
    train_test(train_path=train_path, test_path=test_path)
