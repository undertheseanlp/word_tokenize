# Vietnamese Word Tokenize

![](https://img.shields.io/badge/build-passing-brightgreen.svg) ![](https://img.shields.io/badge/F1-94%25-red.svg)

This repository contains experiments in Vietnamese Word Segmentation problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Table of contents

* [Setup environment](#setup-environment)
* Experiments
  * [Train a new dataset](#train-a-new-dataset)
  
## Setup Environment

Clone project

```
$ git clone https://github.com/undertheseanlp/word_tokenize.git
```

Create environment using conda

```
$ cd word_tokenize
$ conda create -n word_tokenize python=3.5
$ pip install -r requirements.txt
```

## Train a new dataset

```
$ cd word_tokenize
$ source activate word_tokenize
$ python main.py
```

Last update: May 2018