# strings ex_6_03
word=input("Input a word ")
linp=input("Input a letter in the word ")
def str_counter():
    ct = 0
    for letter in word:
        if letter == linp:
            ct=ct+1
    print("Total Letter Count:", ct)
str_counter()