fname=input("Enter File: ")
if len(fname) < 1: fname="clown.txt"
hand=open(fname)

di=dict()
for lin in hand:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds: #retrieve/create/update counter
        di[w] = di.get(w,0) + 1
#print(di)

tmp = list() #new list
for k,v in di.items():
    #print(k,v)
    newt = (v,k) #create new tuple with value/key
    tmp.append(newt)#append to variable tmp
#print("Flipped", tmp)
tmp=sorted(tmp,reverse=True)#sort in reveres lowest to highest
#print("Sorted: ", tmp[:5])#print the top 5
for v,k in tmp[:5]: #make pretty
    print(k,v)
