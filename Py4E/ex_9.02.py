fname=input('Enter File Name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From '):
        words=line.split()
        print(words)
        counts[words[1]] = counts.get(words[1], 0)+1
print(counts) 