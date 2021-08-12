#practice ex_7_05
fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  #strip right side whitepace
    if line.startswith('From:'): #search for value From:
        print(line) #print only line with value From:
