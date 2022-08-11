fhand=open('romeo.txt') #open file
counts=dict() #make a dictionary
for line in fhand: 
    words = line.split()#outer loop split lines into words
    for word in words: #inner loop, loops through words
        counts[word] = counts.get(word,0)+1 # count each word and create histogram
print(counts)
lst=list() #create list from histogram
for key, val in counts.items(): #loop through list
    newtup = (val,key) #create tuple with value first
    lst.append(newtup)
lst=sorted(lst,reverse=True)#sort backwards
print(lst)
for val,key in lst[:10]: #Get the ten most common words
    print(key,val)#print out in key,val form