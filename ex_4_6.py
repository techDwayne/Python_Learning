def computepay(h, r):
    h=float(hrs)
    r=float(rate)
    if h <= 40:
        return r * h
    elif  h > 40:
        return (40 * r) + (h - 40) * (r * 1.5) 

hrs = input("Enter Hours:")
rate=input("Enter Rate:")
p = computepay(10,20)
print("Pay", p)
