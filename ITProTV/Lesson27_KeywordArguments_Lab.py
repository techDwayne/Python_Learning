import csv
with open ("data.csv","w", newline='') as csvFile:
    fieldnames = ['Name','City','State']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
def myData(name,city,state):
    csvData = [name,city,state]
    writer = csv.writer(csvFile)
    writer.writerow(csvData)
char = 'Y'
while char == 'Y':
    name = input("Enter Name:")
    city = input("Enter City:")
    state = input("Enter State:")
    with open ("data.csv","a", newline='') as csvFile:
        myData(name,city,state)
        char = input("Do you want to continue adding records (Y/N):")
filename = 'data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        