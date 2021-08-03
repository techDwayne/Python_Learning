rate = input("Rate of pay: ")
r=float(rate)
hours = input("Hours Worked: ")
h=float(hours)
if h <= 40:
    pay = r * h #calculate normal pay
if h > 40:
        pay= (40 * r) + (h - 40) * (r * 1.5) #calculate overtime pay
print ("Your Pay was:", pay)
