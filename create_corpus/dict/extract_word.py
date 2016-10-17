# -*- coding: utf-8 -*-

import re
import os
word_set1 = set()
word_set2 = set()
word_set = set()

file_list = os.listdir()
word_list = []

for file_dir in file_list:
    with open(file_dir,'rb') as f:
        for line in f:
            try:
                word_list = re.findall(r'([A-Za-z]+)', line.decode("utf-8"))
            except TypeError:
                print (line)
            word_set.update(set(word_list))
            



with open('dic_extracted.txt','w') as f2:
    for word in word_set:
        f2.write(word)
        f2.write("\n")

