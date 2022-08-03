#Program for using default arguments in user-defined function
#User-defined function
def favgame(name, ch="Soccer"):
    print("Hello {}! Your favorite game is {}.".format(name,ch))
#Accept an input
tempname = input("Enter your name:")
#Call the function with only the first argument
print("Calling favgame() with only the name as an argument…")
favgame(tempname)

#Call the function with both the arguments, where the default argument is overwritten with a new value
print("Calling favgame() with both the arguments, where the default argument is overwritten with a new value")
favgame(tempname, "Cricket")

#Code below cannot run, since the function has no arguments
#Call the function with no arguments
#print("Calling favgame() with no argument…")
#favgame()