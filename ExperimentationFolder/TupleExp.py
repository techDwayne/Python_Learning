y = (1, 7, 4, 34, 56, 21, 89)
print(max(y))
print(" ")
print(y[5])
print(" ")
for iter in y:
    print(iter)

(x,y)=(4,"fred")
print(y)
(a,b)=(99,98)
print(a)

#dictionary items() method returns a tuple
d=dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print(k,v)
tups=d.items()
print(tups)

d={'a':10, 'b':1, 'c': 22}
print(d.items())
print(sorted(d.items()))

print(" ")
#sort by key  
d={'a':10, 'b':1, 'c': 22}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)
    
print(" ")
#sort by value

c={'a':10, 'b':1, 'c': 22} 
tmp = list() #create a list of tuples
for k,v in c.items(): #get each key/value pair
    tmp.append((v,k) ) #create new tuple with the value first
print(tmp) #print list of tuples
tmp =sorted(tmp,reverse=True)#sort list of tuples in reverse order
print(tmp)