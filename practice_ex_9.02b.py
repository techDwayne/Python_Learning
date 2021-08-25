#practice_ex_9.02b.py
import string #import the string library

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line=line.translate(line.maketrans('', '', string.punctuation)) #remove punctuation
    line=line.lower()  #changes capital to lower case
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
lst=list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key,counts[key])