#Accept a number as the input
x = 0
for y in [1,2,3]:
    z = int(input("Enter a number:"))
    if z== 0:
        y = y + 1
        continue
    else:
        x = z
        break
flag=False
if x>1:
    for c in range(2,x):
        if(x % c)==0:
            flag=True
if flag:
    print("The entered number is not a prime number.")
else:
    print('The entered number is a prime number.')
    