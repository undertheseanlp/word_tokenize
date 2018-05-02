# Vietnamese Word Segmentation

![](https://img.shields.io/badge/build-passing-brightgreen.svg) ![](https://img.shields.io/badge/F1-94%25-red.svg)

This repository contains experiments in Vietnamese Word Segmentation problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

* [Demo](http://magizbox.com:9386)
* [Detail Report](https://docs.google.com/spreadsheets/d/1i-3WydtRhs8Qmh_-PHxdftQQPnxZ0q4sHhcx8_euNmc/edit?usp=sharing)

# Corpora Summary

Corpus is in [UniversalDependencies format](https://github.com/UniversalDependencies/UD_Vietnamese).

```
# Corpus 1
Documents: 47
Sentences: 7182
Words    : 184005

# Corpus 2
Sentences    : 19692
Unique Words : 20945
```

## Usage

**Setup Environment**

```
# clone project
$ git clone https://github.com/undertheseanlp/word_tokenize.git

# create environment
$ cd word_tokenize
$ conda create -n word_tokenize python=3.5
$ pip install -r requirements.txt
```

**Run Experiments**

```
$ cd word_tokenize
$ source activate word_tokenize
$ python main.py
```

Last update: May 2018