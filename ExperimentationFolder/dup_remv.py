names = ["George", "Fred", "Alice", "Fred", "Sue", "Alice", "George", "George"]
print("Before", names)
names=list(set(names))
print("After", names)
names=sorted(set(names))
print("Sorted", names)

num=(1,2,4,5,6,3,7,4,1,6,8,10,45,32,5,1,7,87,42,31,45,29,1,3,2,5,6)
print("Before: ", num)
print("After: ", list(set(num)))
print("Sorted: ", sorted(list(set(num))))

