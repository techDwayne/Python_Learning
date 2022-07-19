
path= '/GitHub/Python_Learning/ITProTV'
fname=input('File to read?\n')
#file=open(f"{path}/{fname}")
with open(f"{path}/{fname}") as file:
    for line in file:
            print(line)
    #refill the cup
    file.seek(0)
    for line in file:
            print(line)

