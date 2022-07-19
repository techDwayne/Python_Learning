path= '/GitHub/Python_Learning/ExperimentationFolder'
fname=input('Enter file name: \n')
list=open(f'{path}/{fname}')
number_of_characters = 0
for pl in list:
    pl=pl.strip('\n')#strips newline char
    print(pl)
list=open(f'{path}/{fname}')
for line in list:
    line=line.strip('\n')#strips newline char
    words=line.split()
    number_of_characters+=len(line)
print('\n Characters: ', number_of_characters)