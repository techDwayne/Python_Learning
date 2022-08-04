import sys
if __name__ == '__main__':
    numArgs = len(sys.argv)
if numArgs == 1:
        myArg = input("Enter the file name:")
else:
    myArg = sys.argv[1]
    
#Create the dictionary
emails = dict()
#The with block follows. Open the file passed as a command-line argument in the read mode.
with open(myArg,'r') as fhand:
    for line in fhand:
        if line.startswith('From '): 
            line = line.split()
            email=line[1]
            emails[email]=emails.get(email,0)+1
#print(emails)

#loop through the dictionary using a maximum loop to find the largest contributor

largest = None
largest_author = None

for key in emails:
    if largest is None: largest = emails[key]
    
    if largest < emails[key]:
        largest = emails[key]
        largest_author=key
        
print(largest_author,largest)

