#0ur list
letters=list('abcdefghijklmnop')
print(letters)

#how do I get the items I want from a list
selected=letters[2:6]
print(selected)

#How do I get every other letter from the list
evry_other=letters[0:len(letters):2]
print('Every other letter: ', evry_other)

#start at 0-more succinct
e_o_l=letters[::2]
print('Every other letter: ', e_o_l)

#Bonus: Reverse with slicing
rev_letters=letters[::-1]
print('Reversed: ', rev_letters)

#Bonus: Reverse with slicing and every other letter
rev_letters=letters[::-2]
print('Reversed: ', rev_letters)
