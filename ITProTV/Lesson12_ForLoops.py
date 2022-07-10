import enum


edutainer=['Aubri', 'Adam', 'Vonne', 'Justin', 'Daniel']
attempts=range(3)
print('Edutainers:', edutainer)
for edutainer in edutainer:
    print('Edutainer: ', edutainer)
favorite_number = 7
for attempts in attempts:
    guess = int(input('What is my favorite number? \n'))
    if guess==favorite_number:
        print('Winner, Winner Chicken Dinner!')
        break
    else:
        print('Try Again!')
for index,edutainers in enumerate(edutainer):
    print(index, ': ' 
          , edutainer)
    

