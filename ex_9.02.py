fname=input('Enter File Name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From '):
        words=line.split()
        counts[words[2]] = counts.get(words[2], 0)+1
print(counts) 