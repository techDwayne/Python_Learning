#Mathematical operators-- +,-,/,*,%(modulus),**(exponent),//(different type of division--python 3)

print('3+1 is: ', 3+1)
print('3-1 is: ', 3-1)
print('6 / 2 is: ', 6/2) #Type conversion from integer to float
print('7 / 2 is: ', 7/2)
print('7 // 2 is: ', 7//2)#Integer Division
print('7 % 2 is: ', 7%2)#Modulus--gives the remainder only
print('6 % 2 is: ', 6%2)
print('7 * 2 is: ', 7*2)
print('7 ** 2 is: ', 7**2)#exponent
#What about other types
print('a' + 'b')#concatenation
print('Vonne ' * 3)
#what about comparison operators: <, <=, >, >=, ==
print('a'<'b')
print('Is 3 < 4: ', 3<4)
print('Is 3 <= 4: ', 3<=4)
print('Is 3 > 4: ', 3>4)
print('Is 3 >= 4: ', 3>=4)
print('Is 3 = 4: ', 3==4)

word_one='cheese'
word_two='salami'
print('Is cheese < salami: ', word_one <word_two)#dictionary order--
word_one='cheese'
word_two='chest'
print('Is cheese < chest: ', word_one <word_two)