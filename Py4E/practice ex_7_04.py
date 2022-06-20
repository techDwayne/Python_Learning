#practice ex_7_04
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'): #search for value From:
        print(line) #print only line with value From:
