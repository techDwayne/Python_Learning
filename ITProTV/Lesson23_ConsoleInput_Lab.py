#Program for a simple calculator that can add, subtract, multiply, and divide
#Select the desired operation
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
#Enter the desired operation number
opchoice = input("Enter the desired operation no. from the menu (1/2/3/4):")#reads console input and stores in opchoice variable
if (int(opchoice, 10) >= 1 and int(opchoice, 10) <= 4):
    #Accept two numbers from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    #Perform the desired mathematical operation
    if opchoice == '1':
        temp = num1+num2
        print("The sum of the two numbers, {} + {} is: {}".format (num1, num2, temp))
    elif opchoice == '2':
        temp = num1-num2
        print("The difference of the two numbers, {} - {} is: {}".format (num1, num2, temp))
    elif opchoice == '3':
        temp = num1*num2
        print("{} multiplied by {} is: {}".format (num1, num2, temp))
    elif opchoice == '4':
        temp = num1/num2
        print("{} divided by {} is: {}".format (num1, num2, temp))
else:
    print("Invalid operation number")