#!/usr/bin/env bash

/home/anhv/anaconda3/envs/word_tokenize/bin/python3 setup.py build_ext --inplace
mv transformer/* -t .
rm -rf transformer
rm -rf build