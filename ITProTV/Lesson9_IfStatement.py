#if conditional
has_eaten_brussel_sprouts = True

if has_eaten_brussel_sprouts ==True:
    print('Yay!!! Popsicle!!')
    
if has_eaten_brussel_sprouts == False:
    print('Here be your coal')
    
#alternate test of boolean value
has_eaten_brussel_sprouts = False

if has_eaten_brussel_sprouts:
    print('Yay!!! Popsicle!!')
  
if not has_eaten_brussel_sprouts:
    print('Here be your coal')
    
#Else statement
has_eaten_brussel_sprouts = True

if has_eaten_brussel_sprouts:
    print('Yay!!! Popsicle!!')
  
else:
    print('Here be your coal')
    
#Guessing gameish
guess=6

if guess ==6:
    print('You win!!!')
    
elif guess ==7:
    print('Runner UP!')
    
elif guess == 5:
    print('Runner UP!')
else:
    print('uh oh')
