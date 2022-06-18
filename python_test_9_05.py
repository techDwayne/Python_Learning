#python_test_9_05.py
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    if  not line.startswith('From '): continue
    line = line.rstrip()
    line=line.split('@')[1]
    words = line
    for word in words:
        counts[words[1]] = 1
     
print(counts)

