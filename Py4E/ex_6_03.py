# strings ex_6_03
winp=input("Input a word ")
linp=input("Input a letter in the word ")
def str_counter():
    ct = 0
    for letter in winp:
        if letter == linp:
            ct=ct+1
    print(winp)
    print("Total Letter Count:", ct)
str_counter()