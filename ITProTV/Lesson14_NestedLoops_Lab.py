"""
The syntax of a nested for loop is as follows:

for [first counter] in [outer loop]: # Outer loop

[body of the outer loop] # Optional

for [second counter] in [nested loop]: # Nested loop

[body of the nested loop]

The nested for loop works as follows:

The program starts with the outer loop, executing its first iteration.
This first iteration triggers the inner, nested loop, which is run as 
many times as the value of the second counter.
Then the program starts its second iteration of the outer loop thereby 
triggering the nested loop again.
After the nested loop runs to completion, the program returns back to 
the top of the outer loop again.
This process continues until the outer loop runs to completion or a 
break or other statement disrupts the process. Unless the process is 
disrupted, the nested for loop runs for first counter x second counter 
number of times.
"""
#Program to print tables from 1 to 10 in a specific format
for a in range(1, 11):
   print("a =", a, ":", end=" ")
   for b in range(1, 11):
    print("{:2d}".format(a*b), end=" ")
   print()
