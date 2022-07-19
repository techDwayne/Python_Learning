path='/GitHub/Python)Learning/ITProTV'
#Prompt the user to enter a file name
fn = input("Enter the file name:")#The file is opened using the open() function in the read mode
with open(f"{path}/{fn}") as y:
#A for loop is used to read each line in the file
 for x in y:
#Each line in the file is converted to upper case using the upper() function
   z = x.upper()
   print(z)