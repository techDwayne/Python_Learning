
path= '/GitHub/Python_Learning/ITProTV' #open path to file
fname=input('File to read?\n')
#file=open(f"{path}/{fname}")
with open(f"{path}/{fname}") as file: #context manager--will close file without explicit file.close()
    for line in file:
            print(line)
    #refill the cup
    file.seek(0)
    for line in file:
            print(line)

