#Sorting and Reversing Lists
numbers=[31,2,43,0,9,10,10]
letters=['b','c', 'e', 'd']
edutainers = ['Jo', 'Justin', 'Vonne', 'Cherokee']

print('Numbers: ', numbers)
print('Letters: ', letters)
print('Edutainers: ', edutainers)

#How do I put a list in "ascending" order
#numbers.sort()
sorted_numbers=sorted(numbers)
print('Sorted Numbers: ', sorted_numbers)
print('Numbers: ', numbers)

sorted_edutainers=sorted(edutainers)
print('Sorted Edutainers: ', sorted_edutainers)
print('Edutainers: ', edutainers)

sorted_letters=sorted(letters)
print('Sorted Letters: ', sorted_letters)
print('letters: ', letters)

#How do I put a list in 'descending' order
print('Sorted Letters: ', sorted_letters)
des_letters=sorted(letters, reverse=True)
print('Letters: ', letters)
print('Sorted Letters: ', sorted_letters)
print('Descedning Letters: ', des_letters)

#How do I fliep a list (Reversimg)
rev_edutainers=list(reversed(edutainers))
print(edutainers)
print(edutainers[2])
print(rev_edutainers)

edutainers.reverse() #--mutated, the list is reversed in place and will be reversed from this point forward. 
print(edutainers)
print(edutainers[2])