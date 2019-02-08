import json
import re

keys=["title","author","author2","paper","year","date","URL","abstract"]
values=[]
with open ('search.txt', 'rt') as in_file: 
    for line in in_file: 
        x=re.findall("^%[A-Z]",line)
        if x in in_file.read():
            print("true")
        values.append(line.rstrip('\n'))
        
    for element in values:
        dictionary = dict(zip(keys, values))
        print(dictionary)
        print(element)    