#Program to demonstrate the use of functions in random module
print("Importing the random module to access the built-in functions…")
import random
#To generate random numbers between 0 and 1
print("Using the random.random() function to generate 5 random numbers")
for x in range(5):
 print('%02.2f' % random.random())
#To generate numbers in a specific numerical range
#Here value to be taken between 200 to 300
print("Using the random.uniform() function to generate 5 random numbers between 200 and 300")
for d in range(5):
 print('%02.2f' % random.uniform(200,300))
#To generate pseudo-random numbers using a seed
import random
print("Using a seed to generate pseudo-random numbers using random.randint()")
random.seed(10)
for i in range(5):
 print(random.randint(400,450))
print("Using a seed to generate pseudo-random numbers using random.uniform()")
random.seed(10)
for i in range(5):
 print(random.uniform(400,450))
print("Using the same seed to generate pseudo-random numbers using random.randint()")
random.seed(10)
for i in range(5):
 print(random.randint(400,450))