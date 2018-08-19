# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:21:03 2018

@author: Susan shim
wordcounting example of CL HW 1
"""

import re
import nltk
from nltk import sent_tokenize
from collections import Counter
import numpy as np
import math

FILE_PATH = '/Users/ShinAhnjae/Desktop/dory/python/python_practice/BROWN_A1.txt'
QSTRING = "I think I will get the best score in the class hi"
SENT_START = '<s>'
SENT_END = '</s>'

def get_product(probs):
    """given a list of probabilities, return the product
    
    Arguments:
        probs {list} -- list of proabilities
    """
    return np.product(probs)

def text_tokenize(text, regex=r'\W+'):
    """tokenize text into list
    
    Arguments:
        text {str} -- text to tokenize
    
    Keyword Arguments:
        regex {regular expression} -- regex to clean data (default: {r'\W+'})
    """
    text = re.sub(regex, " ", text)
    text = '{start} {text} {end}'.format(start=SENT_START, text=text, end=SENT_END)
    text = text.lower()
    text = text.split()
    return text


def get_bigram_prob(bigram, unigram_count, bigram_count, eps=1e-5):
    """calculate probability of a bigram
    
    Arguments:
        bi {tuple} -- 2 element bigram
    """
    assert len(bigram) == 2
    bigram_prob = (bigram_count[bigram] + eps) * 1.0 / (len(bigram_count) * (1 + eps))
    return bigram_prob

def get_mle_prob(bigram, unigram_count, bigram_count, eps=1e-5):
    """calculate probability of a bigram with MLE
    
    Arguments:
        bigram {tuple} -- 2 element of bigram
        bigram_count {Counter} -- bigram count
        unigram_count {Counter} -- unigram count
    """
    assert len(bigram) == 2
    bigram_prob = (bigram_count[bigram] + eps) * 1.0 / (unigram_count[bigram[0]] + eps * len(unigram_count))
    return bigram_prob


def get_prob_sent(sent, unigram_count, bigram_count, mode='mle'):
    """Given a sentence calculate the probability !
    
    Arguments:
        sent {string} -- string to calculate prob
        bigram_count {Counter} -- Counter of bigram counts
        mode {string} -- one of 'mle' or 'bigram'

        1. tokenize sentence into bigrams
        2. calculate each bigram's probability
        3. calculate the product of the probs.
    """
    assert mode in ('mle', 'bigram')

    sent_split = text_tokenize(sent)
    sent_bigram = nltk.bigrams(sent_split)

    get_prob = get_bigram_prob if mode == 'bigram' else get_mle_prob

    sent_probs = [
        get_prob(bigram, unigram_count, bigram_count) 
            for bigram in sent_bigram
    ]

    probability = get_product(sent_probs)
    return probability

def get_corpus_counts(corpus_path):
    """return a unigram, bigram Counter object of a text corpus file
    
    Arguments:
        file_path {str} -- path to corpus file
    """
    corpus_list = []
    with open(corpus_path, 'r') as corpus:
        for sent in sent_tokenize(corpus.read()):
            sent = text_tokenize(sent)
            corpus_list.extend(sent)
    
    unigram_count = Counter(corpus_list)
    bigram_count = Counter(nltk.bigrams(corpus_list))    

    return unigram_count, bigram_count

def main():
    """
    open file, read the data(data), clear out the other characters and lowercase them
    and split it into a list(data_split)
    """
    unigram_count, bigram_count = get_corpus_counts(FILE_PATH)
    prob = get_prob_sent(QSTRING, unigram_count, bigram_count, mode='mle')
    print(prob)
    
if __name__ == '__main__':
    main()
