# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:21:03 2018

@author: LG
"""
#set current working directory
import os
os.chdir("C:/Users/LG/Desktop/2018-S/fython")
#open file, read the data(data), clear out the other characters and lowercase them
#and split it into a list(data_split)
import re
import nltk
f = open("BROWN_A1.txt", "r")
data = f.read()
data_lower = data.lower()
data_clean = re.sub('/W+','', data_lower)
data_split = data_clean.split()
#open a dictionary
wordcount = {}
#count words in list(data_split), if word already in list, pass, but if not,
#add it to the current wordcount dictionary. Counting frequency
for item in data_split:
    if item in wordcount.keys():
        wordcount[item] += 1
    else:
        wordcount[item] = 1
 
qstring = "I think I will get the best score in the class"
qstring_split = qstring.split()
qstring_dict = {}
for word in qstring_split:
    if word in qstring_dict.keys():
        qstring_dict[word] += 1
    else:
        qstring_dict[word] = 1
#count bigrams in the text file
from nltk import Counter
data_bi = Counter(nltk.bigrams(data_split)) 
q_bi = Counter(nltk.bigrams(qstring_split))
#count the probability of each word in wordcount dictionary
biprob_list = []
for item in q_bi:
    if item in data_bi:
        biprob_list.append(q_bi[item]/data_bi[item])
    else:
        bi_prob = 0
total_prob = 1
for prob in biprob_list:
    total_prob = total_prob * prob

