#!/usr/bin/env python
import sys
import os
from deepmultilingualpunctuation import PunctuationModel
import nltk

import warnings
warnings.filterwarnings("ignore")


def main():
    f = "transcript2.txt"
    model = PunctuationModel()
    tokenizer = nltk.data.load('tokenizers/punkt/french.pickle')


    with open(f, "r") as f:
        text=f.read()
        ## remove empty lines
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        result = model.restore_punctuation(text)
        sentences = [s.capitalize() for s in tokenizer.tokenize(result)]
        text = " ".join(sentences)
        print(text)
        








if __name__ == '__main__':
    
    main()