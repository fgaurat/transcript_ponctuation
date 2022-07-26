#!/usr/bin/env python
import sys
import os
from deepmultilingualpunctuation import PunctuationModel
import warnings
warnings.filterwarnings("ignore")


def main():
    f = "transcript2.txt"
    model = PunctuationModel()


    with open(f, "r") as f:
        text=f.read()
        ## remove empty lines
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        result = model.restore_punctuation(text)
        print(result)







if __name__ == '__main__':
    
    main()