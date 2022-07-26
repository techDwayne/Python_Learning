foods_prompt="""
Which Food are you purchasing? 
A) Banana
B) Apple
C) Cheese
D) Pickles
Q) Quit
"""
while True:
    qty_prompt="""
How many do you need? """

    food=input(foods_prompt) #accept input from user
    if food=="Q":
        print('Goodbye! Come Again!')
        break
    if food not in ['A','B', 'C', 'D']:
        print("Invalid Option, try again.")
    else:
        quantity=int(input(qty_prompt))
        if quantity< 0:
            print('Quantity is incorrect, please re-enter.')
        if food=='A':
            cost = 0.30
            food_label='Banana'
        elif food=='B':
            cost=1.00
            food_label='Apple'
        elif food=='C': 
            cost=3.00
            food_label='Cheese'
        else: 
            cost =2.99
            food_label='Pickles'
        total=cost*quantity 
        result="You are buying: {} {} for ${}".format(quantity,food_label,total)
        print(result)