#Accept a number as the input, int function called to convert string to int
x=int(input("Enter a number:"))
#Use the if-else statement to check whether the entered number is zero, positive, or negative
if x>0:
 print("The entered number is positive")
elif x==0:
 print("The entered number is zero")
else:
 print("The entered number is negative")