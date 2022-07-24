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
    if line.startswith('From '): 
        line = line.split()
        email=line[1]
        email=email.split('@')
        domain=email[1]
        print(domain)
        counts[domain]=counts.get(domain,0)+1
print(counts)

