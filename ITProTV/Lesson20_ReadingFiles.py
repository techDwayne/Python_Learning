
path='\GitHub\Python_Learning\ITProTV'
fname=input('File to read?\n')
file=open(f"{path}/{fname},'r'")
#file=open("\data.txt",'r')
for line in file:
        print(line)

file.close()
