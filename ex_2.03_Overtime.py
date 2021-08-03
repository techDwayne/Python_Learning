hrs = input("Enter Hours: ")
h=float(hrs)
rate = input("Enter Pay Rate: ")
r=float(rate)
if h <= 40:
    pay = r * h #calculate normal pay
if h > 40:
        pay= (40 * r) + (h - 40) * (r * 1.5) #calculate overtime pay
print ("Your Pay was:", pay)
