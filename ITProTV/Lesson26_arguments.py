#define function
def eat(food=None,happy=False): #default argument, default value for argument
    if happy:
        print("Yayyy!!!")
    
    if food is None:
        print("Nom Nom!!")
    
    else:  
        print("I just had some {}!".format(food))
    

eat('cheese', True)
eat()