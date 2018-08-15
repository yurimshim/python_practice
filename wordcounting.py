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
#count bigrams in the text file
bigram = list(nltk.bigrams(data_split))        
qstring = "I think I will get the best score in the class"
qstring_split = qstring.split()
qstring_dict = {}
for word in qstring_split:
    if word in qstring_dict.keys():
        qstring_dict[word] += 1
    else:
        qstring_dict[word] = 1
#count the probability of each word in wordcount dictionary
for key in qstring_dict.keys():
    if key in wordcount.keys():
        key_prob = qstring_dict[key]/wordcount[key]
    else:
        key_prob = 0
#
