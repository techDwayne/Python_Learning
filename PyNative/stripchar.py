
# Python3 code to demonstrate 
# how to remove 'n' characters from starting
# of a string
  
# Initialising string
ini_string1 = input("Input?")
  
# Initialising number of characters to be removed
char = input("Number of characters to remove?")
n=int(char) 
# Printing initial string
print ("Initial String", ini_string1)
  
# Removing n characters from string
print("Removing characters from a string.")
print(ini_string1[n:])
