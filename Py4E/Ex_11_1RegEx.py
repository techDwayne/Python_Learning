import re


fhand=open('regex_sum_1317280.txt')
number = []
count = 0
for line in fhand:
    line=line.rstrip()
    x = re.findall('[0-9]+', line)
    
    if len(x)>0:
        print(x)
        number=number + x
print(number)
total = 0
for item in number:
    item=int(item)
    print(item)
    total = total + item
    count += 1
print(count)
print(total)