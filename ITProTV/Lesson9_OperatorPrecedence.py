#membership tests
edutainers=['Vonne', 'Justin', 'Aubri', 'Ronnie']
print('Daniel in Edutainers: ', 'Daniel'in edutainers)
print('Vonne in Edutainers: ', 'Vonne'in edutainers)
print('Daniel in Edutainers: ', 'Daniel' not in edutainers)

#Identity Tests
favorite_food= 'cheese'
lunch_today = 'cheese'
print(favorite_food is lunch_today)
other_edutainers = ['Vonne', 'Justin', 'Aubri', 'Ronnie']
print(edutainers is other_edutainers)

#not operator
print(not 1==1)


#precedence--math before comparison
print(3 % 2 + 1 == 4 - 2 // 3)


#precedence--math before comparison
print(4*3+1)

