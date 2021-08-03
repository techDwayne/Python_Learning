hrs = input("Enter Hours: ")
h=float(hrs)
rate = input("Enter Pay Rate: ")
r=float(rate)
if h <= 40:
    pay = r * h
    print (pay)
elif  h > 40:
    pay= (40 * r) + (h - 40) * (r * 1.5) 
print (pay)
