import string

fname=input('Enter File Name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From '):
        line=line.rstrip()
        line=line.translate(line.maketrans('.', '@', string.punctuation))
        words=line.split()
        counts[words[1]] = counts.get(words[1], 0)+1
print(counts)