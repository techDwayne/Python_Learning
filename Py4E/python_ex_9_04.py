#python_test_9_05.py
import string
most_mail = 0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
#Create the dictionary
counts = dict()
for line in fhand:
    if line.startswith('From '): 
        line = line.split()
        email=line[1]
        #email=email.split('@')
        #print(email)
        #domain=email[1]
        domain=email
        counts[domain]=counts.get(domain,0)+1
#print(counts)

#loop through the dictionary using a maximum loop to find the largest contributor
largest = None
largest_author = None

for key in counts:
    if largest is None: largest = counts[key]
    if largest < counts[key]:
        largest = counts[key]
        largest_author=key
        
print(largest_author,largest)

