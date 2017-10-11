# Word Segmentation Experiments

This repository contains experiments in Vietnamese Word Segmentation problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) - a Vietnamese NLP Toolkit

# Corpora Summary

Corpus 1

```
Documents: 47
Sentences: 7182
Words    : 184005
```

Corpus 2

```
Sentences    : 19692
Unique Words : 20945
```

## Reports

![](https://img.shields.io/badge/F1-94%25-red.svg)

* [Detail Reports](https://docs.google.com/spreadsheets/d/1i-3WydtRhs8Qmh_-PHxdftQQPnxZ0q4sHhcx8_euNmc/edit?usp=sharing)

## Usage

**Setup Environment**

```
# clone project
$ git clone git@github.com:magizbox/underthesea.word_sent.git

# create environment
$ cd underthesea.word_sent
$ conda create -n uts.word_sent python=3.4
$ pip install -r requirements.txt
```

**Run experiment**

```
$ cd underthesea.word_sent
$ source activate uts.word_sent
$ python main.py
```

## Related Works

* [Vietnamese Word Segmentation Tools](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Tools#word-segmentation)
* [Vietnamese Word Segmentation Publications](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Publications#word-segmentation)
* [Vietnamese Word Segmentation State of The Art](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-SOTA#word-segmentation)
* [Vietnamese Word Segmentation Service](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Services#word-segmentation)

Last update: October 2017