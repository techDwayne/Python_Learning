
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
#Create the dictionary
counts = dict()
for line in fhand:#loops through the file
    if line.startswith('From '): #find each FROM line
        line = line.split() #split the line
        time=line[5] #split out the time in each line
        hms=time.split(':') #split time at each :      
        hour=hms[0]#split out the hour 
        counts[hour]=counts.get(hour,0)+1#add the hour and the count to the dictionary
lst=list() #create list from histogram
for key, val in counts.items(): #loop through list
    newtup = (key, val) #create tuple 
    lst.append(newtup)#append the list with each tuple
lst=sorted(lst)#sort the list
for val,key in lst: #loop through the sorted list
    print(val,key)#print out in val,key form

    




