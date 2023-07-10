


# user input
n = input("Number? ")
num=int(n)

#if number is divisible by 3, return "Fizz"
#if number is divisible by 5, return "Buzz"
#if number is divisible by 3 and 5, return "FizzBuzz"

def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num
print(fizz_buzz(num))

