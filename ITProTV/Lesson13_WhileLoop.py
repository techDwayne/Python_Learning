#favorite_phrase='I like Cheese'
#for letter in favorite_phrase:
#    print(letter)
#index=0
#while index<len(favorite_phrase):
#    letter=favorite_phrase[index]
#    print(letter)
#    index=index+1

from math import fabs


favorite_number = 7
running=True
while running:
    guess=int(input("What is Vonne's favorite number?\n"))
    if guess==favorite_number:
        print('Yayyyy!!! You Win!!!!')
        running=False
    else:
        print("Try Again!")
    