#Program for a simple calculator that can add, subtract, multiply, and divide
#Select the desired operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#Enter the desired operation number
opchoice = input("Enter the desired operation no. from the menu (1/2/3/4):")
#if (int(opchoice, 10) >= 1 and int(opchoice, 10) <= 4):
 #Accept two numbers from the user
 #num1 = int(input("Enter first number: "))
 #num2 = int(input("Enter second number: "))
 #Perform the desired mathematical operation
 #if opchoice == '1':
  #temp = num1+num2
  #print("The sum of the two numbers, {} + {} is: {}".format (num1, num2, temp))
 #elif opchoice == '2':
  #temp = num1-num2
  #print("The difference of the two numbers, {} - {} is: {}".format (num1, num2, temp))
 #elif opchoice == '3':
  #temp = num1*num2
  #print("{} multiplied by {} is: {}".format (num1, num2, temp))
 #elif opchoice == '4':
  #temp = num1/num2
  #print("{} divided by {} is: {}".format (num1, num2, temp))
#else:
  #print("Invalid operation number")
#User-defined functions
#This function adds two numbers and prints the result
def add(x, y):
    temp = x + y
    print("The sum of the two numbers, {} + {} is: {}".format(x, y, temp))
#This function subtracts two numbers and prints the result
def subtract(x, y):
    temp = x - y
    print("The difference of the two numbers, {} - {} is: {}".format(x, y, temp))
#This function multiplies two numbers and prints the result
def multiply(x, y):
    temp = x * y
    print("{} multiplied by {} is: {}".format(x, y, temp))
#This function divides two numbers and prints the result
def divide(x, y):
    temp = x/y
    print("{} divided by {} is: {}".format(x, y, temp))

if (int(opchoice, 10) >= 1 and int(opchoice, 10) <= 4):
 #Accept two numbers from the user
 x = int(input("Enter first number:"))
 y = int(input("Enter second number:"))
 #Perform the desired mathematical operation and call the functions
if opchoice == '1':
    add(x,y)
elif opchoice == '2':
    subtract(x,y)
elif opchoice == '3':
    multiply(x,y)
elif opchoice == '4':
    divide(x,y)
else:
    print("Invalid operation number")
