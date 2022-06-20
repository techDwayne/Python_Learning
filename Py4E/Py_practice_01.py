fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' : continue
    count=count + 1
    print(words[2])
print("There were", count,  "lines with From as the first word.")