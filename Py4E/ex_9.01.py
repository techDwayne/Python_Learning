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
        counts[words[1]] = counts.get(words[1], 0)+1
bigcount=None
bigmail=None

for count in counts:
    if bigcount is None:  bigcount=counts[count]
    if bigcount < counts[count]:
        bigcount=counts[count]
        bigmail = count
print(bigmail, bigcount) 