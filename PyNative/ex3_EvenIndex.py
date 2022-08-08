origStr=input("Input? ")
print("Original string is:", origStr)
#print(OrigStr)

str1=list(origStr)
print(str1)
print("Printing only even index chars")
for i in str1[0::2]:
    print(i)
