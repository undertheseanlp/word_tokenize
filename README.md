# Vietnamese Word Tokenize ![](https://img.shields.io/badge/F1-94%25-red.svg)

This repository contains experiments in Vietnamese Word Segmentation problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Table of contents

* [Installation](#installation)
  * [Requirements](#requirements)
  * [Download and Setup Environement](#download-and-setup-environment)
* [Usage](#usage)
  * [Using a pretrained model](#using-a-pretrained-model)
  * [Train a new dataset](#train-a-new-dataset)
  * [Sharing a model](#sharing-a-model)
* [Citation](#citation)

## Installation

### Requirements

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.5+`
* `Anaconda`
* `languageflow==1.1.7`

### Download and Setup Environment

Clone project using git

```
$ git clone https://github.com/undertheseanlp/word_tokenize.git
```

Create environment and install requirements

```
$ cd word_tokenize
$ conda create -n word_tokenize python=3.5
$ pip install -r requirements.txt
```

## Usage

### Using a pretrained model

```
python word_tokenize.py -fin tmp/input.txt -fout tmp/output.txt
python word_tokenize.py -in "Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò"
```

### Train a new dataset

**Prepare a new dataset**

**Train and test**

```
$ cd word_tokenize
$ source activate word_tokenize
$ python train.py \
    --train data/vlsp2016/corpus/train.txt
```

### Sharing a model

To be updated

Last update: May 2018