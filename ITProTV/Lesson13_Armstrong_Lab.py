#Program to check Armstrong numbers in certain interval
#To accept an interval as input from the user
lower = int(input("Enter lower range:"))
upper = int(input("Enter upper range:"))
for num in range(lower, upper + 1):
    #Calculate the order of number
    order = len(str(num))
    #Initialize sum
    sum = 0
    #Find the sum of the order of each digit
    temp = num
    while temp > 0:
        #Find remainder
        digit = temp % 10
        #Find the order of digits and add it to the sum
        sum += digit ** order
        temp //= 10
#If num matches the sum, print it as Armstrong number
    if num == sum:
        print(num, "is an Armstrong number.")