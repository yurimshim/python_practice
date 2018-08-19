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

FILE_PATH = '/Users/ShinAhnjae/Desktop/dory/python/python_practice/BROWN_A1.txt'
QSTRING = "I think I will get the best score in the class"

SENT_START = '<s>'
SENT_END = '</s>'

# P(I | <s>) * P(think | I) * P(I | think) ....

def get_product(probs):
    """given a list of probabilities, return the product
    
    Arguments:
        probs {list} -- list of proabilities
    """
    return np.product(probs)

def get_bigram_prob(bigram, unigram_count, bigram_count):
    """calculate probability of a bigram
    
    Arguments:
        bi {tuple} -- 2 element bigram
    """
    assert len(bigram) == 2
    bigram_prob = bigram_count[bigram] * 1.0 / len(bigram_count)
    return bigram_prob

def get_mle_prob(bigram, unigram_count, bigram_count):
    """calculate probability of a bigram with MLE
    
    Arguments:
        bigram {tuple} -- 2 element of bigram
        bigram_count {Counter} -- bigram count
        unigram_count {Counter} -- unigram count
    """
    assert len(bigram) == 2
    print(bigram)
    bigram_prob = bigram_count[bigram] * 1.0 / unigram_count[bigram[0]]
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

    sent = re.sub("/W+", " ", sent)
    sent = SENT_START + ' ' + sent + ' ' + SENT_END
    sent = sent.lower()
    sent_split = sent.split()
    sent_bigram = nltk.bigrams(sent_split)

    sent_probs = []
    for bigram in sent_bigram:
        if mode == 'bigram':
            bigram_prob = get_bigram_prob(bigram, unigram_count, bigram_count)
        elif mode == 'mle':
            bigram_prob = get_mle_prob(bigram, unigram_count, bigram_count)
        else:
            raise Exception('mode should be one of bigram, mle')

        sent_probs.append(bigram_prob)

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
            sent = re.sub(r'\W+', ' ', sent) # string
            sent = sent.lower() # string
            sent = SENT_START + ' ' + sent + ' ' + SENT_END # string
            sent = sent.split() # list of words
            corpus_list.extend(sent) # list of words
    
    unigram_count = Counter(corpus_list)
    bigram_count = Counter(nltk.bigrams(corpus_list))    
    return unigram_count, bigram_count

def main():
    """
    open file, read the data(data), clear out the other characters and lowercase them
    and split it into a list(data_split)
    """
    unigram_count, bigram_count = get_corpus_counts(FILE_PATH)
    prob = get_prob_sent(QSTRING, unigram_count, bigram_count, mode='bigram')
    print(prob)
    
if __name__ == '__main__':
    main()
