fname=input('Enter File Name: ')
try:
    fhand=open(fname)
except: 
    print("File cannot be found.", fname)
    exit()
counts=dict()
for line in fhand:
    if line.startswith('From '):
        words=line.split()
        print(words)
        counts[words[2]] = counts.get(words[2], 0)+1
bigcount=None
bigmail=None

for count in counts:
    if bigcount is None:  bigcount=counts[count]
    if bigcount < counts[count]:
        bigcount=counts[count]
        bigmail = count
print(bigmail, bigcount) 