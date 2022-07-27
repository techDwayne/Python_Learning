largest=None
print('Before: ', None)
for intervar in[3,4,12,9, 74, 16]:
    if largest is None or intervar > largest:
        largest=intervar
    print("Loop: ", intervar, largest)
print("Largest: ",largest)