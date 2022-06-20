count = 0
words_list = dict()                   # Initializes the dictionary
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in words_list:
            continue                        # Discards duplicates
        words_list[word] = count      # Value is first time word appears

if 'julie' in words_list:
    print('True')
else:
    print('False')
print(words_list)