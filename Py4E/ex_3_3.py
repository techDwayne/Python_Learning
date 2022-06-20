score = input("Enter Score: ")
try:
    scr=float(score)
except:
    print ("Sorry, you must enter a numeric value.")
    quit()
if scr >= 0.9:
    print('A')
elif scr >= 0.8:
    print ('B')
elif scr >= 0.7:
    print ('C')
elif scr >= 0.6:
    print ('D')
elif scr < 0.6:
    print ('F')

