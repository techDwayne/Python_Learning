fname=input('Enter File Name: ') 
try:
    fhand=open(fname)
except: 
    print("File cannot be found.", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('From: '):
        words=line.split()
        count=count+1
        print(words[1])
print("There were", count, "lines in the file with From as the first word")
