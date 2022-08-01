import sys

filenamem = sys.argv[0]
arguments = sys.argv[1:]
food=arguments[0]
quantity=int(arguments[1])
cost=float(arguments[2])

total=quantity*cost
print("You are bying {} {} for ${}".format(quantity,food,total))
