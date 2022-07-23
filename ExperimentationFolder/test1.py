astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(astr)
print(istr)
def thing():
    print('Hello')
 
print('There')
def func(x) :
    print(x)
 
func(10)
func(20)
def stuff():
    print('Hello')
    return
    print('World')
 
stuff()
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
 
print(greet('fr'),'Michael')
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])
print(len('banana')*7)
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
