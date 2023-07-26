names = ["George", "Fred", "Alice", "Fred", "Sue", "Alice", "George", "George"]
print("Before", names)
names=list(set(names))
print("After", names)
names=sorted(set(names))
print("Sorted", names)
