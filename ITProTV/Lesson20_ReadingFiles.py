
path= '/GitHub/Python_Learning/ITProTV'
fname=input('File to read?\n')
file=open(f"{path}/{fname}")
lines=file.readlines()
#file=open('data.txt','r')
for line in lines:
        print(line)
for line in lines:
        print(line)
file.close()
