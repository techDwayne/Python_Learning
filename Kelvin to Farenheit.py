# convert Kelvin to Farenheit

def keltofah(k):  #function to convert Kelvin to Farenheit
    return (k-273.15) * 1.8 + 32

print('Enter Temperature in Kelvin: ')
kel=float(input())
farenheit=keltofah(kel)
print('\n Equivalent Temperature in Farenheit = {:0f}'.format(farenheit))

