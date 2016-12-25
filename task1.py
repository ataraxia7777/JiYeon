#-*-coding: utf-8 -*-

import sys
import csv
import re
import os # for making a file
from collections import Counter
from collections import OrderedDict

cnt = Counter()
#ifp = open('C:\\Users\\Y -CERT5\\Documents\\CTF1.log','r',encoding = 'ASCII')
with open('C:\\Users\\Y -CERT5\\Documents\\CTF11.txt') as ifp: #opening file and making long list
 fin = []

 for line in ifp:  #for each line
      
       result = re.findall(r"\d*[.]\d{1,3}[.]\d{1,3}[.]\d*",line)
       fin.extend(result)
       
        
fin = list(set(fin))

with open('./test_file1.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fin)
