## our first list
edutainers = ['Adam', 'Aubri', 'Daniel', 'Jo', 'Justin', 'Zach']
print("Edutainers: ", edutainers)
print('The third edutainter is: ', edutainers[2])
#How do I know how many elements there are programatically
print('The number of edutainers is: ', len(edutainers))
#use with string
print('Justin has ',len('Justin'), 'characters in his name.')
#or use element position
print('Justin has ',len(edutainers[4]), 'characters in their name.')

#How do I convert a string (others can apply) to a list?
favorite_food='fish taco'
favorite_food_character_list=list(favorite_food)
print('Favorite Food: ', favorite_food_character_list)
print('Characters: ', favorite_food)



