#practice ex_7_07
fhand = open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()  
    if line.find('@uct.ac.za') == -1: continue
    #find returns either line position or -1, continue tells it to execute the next line
    print(line)