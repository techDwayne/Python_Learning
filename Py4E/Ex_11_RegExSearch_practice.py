import re
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
#Create the dictionary
counts = dict()
for line in fhand:
    line=line.rstrip()
    if re.search('^From:.+@', line):#Search using RegEx
        line=line.split()#splits line into a list
        email=line[1]
        counts[email]=counts.get(email,0)+1
        #print(counts)
lst=list() #create list from histogram
for key, val in counts.items(): #loop through list
    newtup = (val,key) #create tuple with value first
    lst.append(newtup)
lst=sorted(lst,reverse=True)#sort backwards
#print(lst)
for val,key in lst[:1]: #Get the most common email
    print(key,val)#print out in key,val form