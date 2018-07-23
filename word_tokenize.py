import argparse

from util.crf.word_tokenize import word_tokenize

parser = argparse.ArgumentParser("word_tokenize.py")
text_group = parser.add_argument_group("The following arguments are mandatory for text option")
text_group.add_argument("--text", metavar="TEXT", help="text to predict")
file_group = parser.add_argument_group("The following arguments are mandatory for file option")
file_group.add_argument("--fin", help="file input")
file_group.add_argument("--fout", help="file output")

args = parser.parse_args()

if __name__ == '__main__':
    if not (args.text or args.fin):
        parser.print_help()

    if args.text:
        text = args.text
        label = word_tokenize(text, format="text")
        print(label)