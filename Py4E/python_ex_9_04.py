
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
#Create the dictionary
emails = dict()
for line in fhand:
    if line.startswith('From '): 
        line = line.split()
        email=line[1]
        emails[email]=emails.get(email,0)+1
print(emails)

#loop through the dictionary using a maximum loop to find the largest contributor
largest = None
largest_author = None

for key in emails:
    if largest is None: largest = emails[key]
    if largest < emails[key]:
        largest = emails[key]
        largest_author=key
        
print(largest_author,largest)

