
fname=input('Enter file name: \n')

list=open(fname)
number_of_characters = 0
for line in list:
    line=line.strip('\n')
    words=line.split()
    number_of_characters+=len(line)
print('Characters: ', number_of_characters)