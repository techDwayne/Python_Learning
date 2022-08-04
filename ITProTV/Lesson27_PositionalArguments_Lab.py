import csv
with open ("data2.csv","w", newline='') as csvFile:
    fieldnames = ['Name','City','State']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
def myData(name,city,state):
    csvData = [name,city,state]
    writer = csv.writer(csvFile)
    writer.writerow(csvData)

name = input("Enter Name:")
city = input("Enter City:")
state = input("Enter State:")
with open ("data2.csv","a", newline='') as csvFile:
    myData(city=city, name=name, state=state)
    myData(state=state,city=city,name=name)
    myData(name=name,city=city,state=state)
filename = 'data2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        