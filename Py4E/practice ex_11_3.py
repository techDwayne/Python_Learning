import re

fname = input('File to open?')
fhand = open(fname)
number=[]
count=0
for line in fhand:
    line =  line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        #print(x)
        number=number + x
#print(number)     
total = 0
for item in number:
    item=int(item)
    #print(item)
    total = total + item
    count += 1
    avg = total//count
print("Count: ", count)
print("Total: ",total)
print("Average: ", avg)