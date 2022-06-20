#compute average, max, min, sum using a list with user input
numlist=list()
while True:
    inp=input('Enter a number: ', )
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
mx=max(numlist)
mn=min(numlist)
total=sum(numlist)
print('Average: ', average)
print('Maximum: ', mx)
print('Minimum: ', mn)
print('Total: ', total )
