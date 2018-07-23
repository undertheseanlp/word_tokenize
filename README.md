# Vietnamese Word Tokenize ![](https://img.shields.io/badge/F1-94%25-red.svg)

This repository contains starter code for training and evaluating machine learning models in *Vietnamese Word Segmentation* problem. It is a part of [underthesea](https://github.com/magizbox/underthesea) project. The code gives an end-to-end working example for reading datasets, training machine learning models, and evaluating performance of the models. It can easily be extended to train your own custom-defined models.

## Table of contents

* [1. Installation](#1-installation)
  * [1.1 Requirements](#11-requirements)
  * [1.2 Download and Setup Environement](#12-download-and-setup-environment)
* [2. Usage](#2-usage)
  * [2.1 Using a pretrained model](#21-using-a-pretrained-model)
  * [2.2 Train a new dataset](#22-train-a-new-dataset)
  * [2.3 Sharing a model](#23-sharing-a-model)
* [3. References](#3-references)


## 1. Installation

### 1.1 Requirements

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.6`
* `Anaconda`
* `languageflow==1.1.7`

### 1.2 Download and Setup Environment

Clone project using git

```
$ git clone https://github.com/undertheseanlp/word_tokenize.git
```

Create environment and install requirements

```
$ cd word_tokenize
$ conda create -n word_tokenize python=3.6
$ pip install -r requirements.txt
```

## 2. Usage

Make sure you are in `word_tokenize` folder and activate `word_tokenize` environment

```
$ cd word_tokenize
$ source activate word_tokenize
``` 

### 2.1 Using a pretrained model

```
$ python word_tokenize.py -fin tmp/input.txt -fout tmp/output.txt
$ python word_tokenize.py -in "Chàng trai 9X Quảng Trị khởi nghiệp từ nấm sò"
```

### 2.2 Train a new dataset

**Train and test**

```
$ python util/preprocess_vlsp2016.py
$ python train.py --mode train \
    --train tmp/vlsp2016/train.txt \
    -s tmp/model.bin
```

### 2.2 Train a new dataset

To be updated

## 3. References

To be updated

Last update: May 2018