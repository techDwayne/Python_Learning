# convert Temperature

def keltofah(k):  #function to convert Kelvin to Fahrenheit
    return (k-273.15) * 1.8 + 32

def fahtokel(f):  #function to converet Fahrenheit to Kelvin
    return (f-32) /1.8 + 273.15

def fahtocel(c): #function to convert Fahrenheit to Celsius
    return (c-32)/1.8 

def celtofah(ft): #function to convert Celsius to Fahrenheit
    return(ft*1.8)+ 32

def celtokel(ck): #function to convert Celsius to Kelvin
    return(ck+32)

def keltocel(kc): #function to convert Kelvin to Celsius
    return(kc-273.15)

temp=input('F, C, or K: ')

if temp=='K':   
    print('Enter Temperature: ')
    kel=float(input())
    fahrenheit=keltofah(kel)
    cels=keltocel(kel)
    print('\n Equivalent Temperature in Farenheit = {:2f}'.format(fahrenheit))
    print('\n Equivalent Temperature in Celsius = {:2f}'.format(cels))
elif temp=='C':
    print('Enter Temperature: ')
    fah=float(input())
    fahrenheit=celtofah(fah)
    kelv=celtokel(fah)
    print('\n Equivalent Temperature in Farenheit = {:2f}'.format(fahrenheit))
    print('\n Equivalent Temperature in Kelvin = {:2f}'.format(kelv))  
else:
    print('Enter Temperature: ')
    fah=float(input())
    kelvin=fahtokel(fah)
    celsius=fahtocel(fah)
    print('\n Equivalent Temperature in Kelvin = {:2f}'.format(kelvin))
    print('\n Equivalent Temperature in Celsius = {:2f}'.format(celsius))

    