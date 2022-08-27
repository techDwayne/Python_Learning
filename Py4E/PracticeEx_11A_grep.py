import re

fhand=open('mbox.txt')
regex = input('Input RegEX to search for:')
count = 0
for line in fhand:
    if re.search(regex, line):
        count += 1
print("mbox.txt had ", count, " lines that matched", regex)
