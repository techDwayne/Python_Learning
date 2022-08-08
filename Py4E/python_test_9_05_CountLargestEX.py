#python_test_9_05.py
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
most_email=0
counts = dict()
for line in fhand:
    if line.startswith('From '): 
        line = line.split()
        email=line[1]
        #email=email.split('@')
        print(email)
        #domain=email[1]
        #domain=email--unecessary variable swapout
        #counts[domain]=counts.get(domain,0)+1--unecessary
        counts[email]=counts.get(email,0)+1 #works flawlessly, reduces lines of code
print(counts)

#loop through the dictionary using a maximum loop to find the largest contributor

largest = None
largest_author = None

for key in counts:
    
    if largest is None: largest = counts[key]
    
    if largest < counts[key]:
        largest = counts[key]
        largest_author=key
        
print(largest_author,largest)

