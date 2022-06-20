#practice ex_8_02.py
abc='With Three Words'
stuff= abc.split() #splits at white space
print(stuff)
print(len(stuff)) #gets the length 
print(stuff[0]) #prints element in 0 position
stuff.sort() #sorts alpha
print(stuff)
for w in stuff: #loop through list
    print(w) #print element in each loop

