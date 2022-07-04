#Enter a year as the input
y=int(input("Enter a year:"))
#Check if the entered year is a leap year
if (y%4)==0:
 if (y%100)==0:
  if (y%400)==0:
   print("The entered year is a leap year")
  else:
   print("The entered year is not a leap year")
 else:
  print("The entered year is a leap year")
else:
 print("The entered year is not a leap year")