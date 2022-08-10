dogs=[]
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print(f"Hello, ", dog, "!")
print("I love these dogs!")

print("\nThese were my first two dogs: ")
old_dogs=dogs[:2]
for old_dog in old_dogs:
    print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)