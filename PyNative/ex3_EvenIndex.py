orig=input("Input? ")
print("Original string is:", orig)
#print(str1)

str1=list(orig)
print(str1)
print("Printing only even index chars")
for i in str1[0::2]:
    print(i)
