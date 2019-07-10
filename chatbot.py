# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import pandas as pd

file = pd.read_csv('friendschat.txt',sep='\t')
lines = file['line']

print('Initial chats')
for i in range(10):
    print(lines[i])
    
def cleanchat(line):
    #to convert text to lower case
    line = line.lower()
    #to remove ending EOL
    line = re.sub(r'\n','',line) 
    #re-format punctuations
    line = re.sub(r"[-()]", "", line)
    line = re.sub(r"\.", " .", line)
    line = re.sub(r"\!", " !", line)
    line = re.sub(r"\?", " ?", line)
    line = re.sub(r"\,", " ,", line)
    
    #string replacement
    line = re.sub(r"i'm", "i am", line)
    line = re.sub(r"he's", "he is", line)
    line = re.sub(r"she's", "she is", line)
    line = re.sub(r"it's", "it is", line)
    line = re.sub(r"that's", "that is", line)
    line = re.sub(r"what's", "that is", line)
    line = re.sub(r"\'ll", " will", line)
    line = re.sub(r"\'re", " are", line)
    line = re.sub(r"won't", "will not", line)
    line = re.sub(r"can't", "cannot", line)
    line = re.sub(r"n't", " not", line)
    line = re.sub(r"n'", "ng", line)
    line = re.sub(r"ohh", "oh", line)
    line = re.sub(r"ohhh", "oh", line)
    line = re.sub(r"ohhhh", "oh", line)
    line = re.sub(r"ohhhhh", "oh", line)
    line = re.sub(r"ohhhhhh", "oh", line)
    line = re.sub(r"ahh", "ah", line)
    
    return line

def preprocess(x):
    return cleanchat(x)

lines['processed_text'] = lines['line'].apply(preprocess)
    
    
    