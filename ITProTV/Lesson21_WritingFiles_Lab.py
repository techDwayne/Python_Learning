#Prompt the user to enter a file name
fn = input("Enter the file name:")
#The file is opened using the open() function in the read mode
with open(fn ,'r') as y:
#A for loop is used to read each line in the file
 for x in y:
#Each line in the file is converted to upper case using the upper() function
  z = x.upper()
  print(z)
#To open the file
#x = open(fn)
#for y in x:
 #z = y.upper()
 #print(z)
#To close the file
#x.close()
#Copy the content from the existing sample.txt file and paste into the new copy.txt file
with open("sample.txt") as r:
 with open("copy.txt", "w+") as r1:
  for x in r:
   r1.write(x)
#Print the contents of copy.txt file
print("Printing the contents of the copy.txt file…")
with open("copy.txt") as r:
 for x in r:
  print(x)