from os import makedirs
from os.path import dirname, join
from languageflow.reader.tagged_corpus import TaggedCorpus
import argparse


def load_data(file):
    tagged_corpus = TaggedCorpus()
    tagged_corpus.load(file)
    sentences = tagged_corpus.sentences
    return sentences


def preprocess(sentences):
    def process_token(t):
        tokens = t[0].split("_")
        tokens = [token for i, token in enumerate(tokens)]
        output = [[token, "B-W"] if i == 0 else [token, "I-W"] for i, token in enumerate(tokens)]
        return output

    def flat_list(l):
        return [item for sublist in l for item in sublist]

    def process_sentence(s):
        tokens = [process_token(t) for t in s]
        output = flat_list(tokens)
        return output

    return [process_sentence(s) for s in sentences]


def raw_to_corpus(sample, output):
    if output:
        output_folder = output
    else:
        output_folder = join(dirname(dirname(__file__)), "tmp", "vlsp2016")
    for f in ["train.txt", "dev.txt", "test.txt"]:
        input = join(dirname(dirname(__file__)), "data", "vlsp2016", "raw", f)
        tagged_corpus = TaggedCorpus()
        tagged_corpus.load(input)
        sentences = tagged_corpus.sentences
        if sample:
            sentences = sentences[:sample]
        tagged_corpus.sentences = preprocess(sentences)
        try:
            makedirs(output_folder)
        except:
            pass
        output_data = join(output_folder, f)
        tagged_corpus.save(output_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("preprocess_vlsp2016.py")
    parser.add_argument("--sample", help="sample size", type=int)
    parser.add_argument("--output", help="output path")
    args = parser.parse_args()
    if args.sample:
        if not args.output:
            parser.error("You must set --output when use option --sample")
    raw_to_corpus(sample=args.sample, output=args.output)
