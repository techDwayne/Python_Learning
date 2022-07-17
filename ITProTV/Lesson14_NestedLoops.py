#numbers=range(1,5) #1,2,3,4
#letters='abcd'

#for number,letter in zip(numbers,letters):
#    print(number,letter)

#for number in numbers:
#   for letter in letters:
#        print(number,letter)
#

days=[
    list(range(3)),
    list(range(4)),
    list(range(5))
]
total=0
for day in days:
    for sale in day:
        print(total, ': ', sale)
        total=total+sale
print(total)