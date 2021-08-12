#practice ex_7_06
fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  
    #skip unintersting lines
    if not line.startswith('From:'):
        continue
        #process our interesting line
    print(line) #print only line with value From: