import re

fhand=open('regex_sum_1317280.txt')
number = []#create empy list
count = 0 #initiate count variable
for line in fhand:
    line=line.rstrip()
    x = re.findall('[0-9]+', line) #find numbers in text file using regex
    
    if len(x)>0:
        print(x)
        number=number + x #add number to list
print(number)
total = 0 #intitate total variable
for item in number: #iterate through the list
    item=int(item) #convert string in list to integer
    print(item)
    total = total + item #add integer to total variable until it reaches the end
    count += 1 #increment count variable
print(count)
print(total)