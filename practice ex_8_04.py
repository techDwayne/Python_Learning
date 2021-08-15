#practice ex_8_04
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print(line.rstrip())