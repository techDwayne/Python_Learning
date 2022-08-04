import csv
with open ("data.csv", w, newline='') as csvfile:
    fieldnames=['Name', 'City', 'State']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader
