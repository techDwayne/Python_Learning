#practice ex_7_10
fname=input('Enter File Name: ') #prompt for file name
try:
    fhand=open(fname)
except: 
    print("File cannot be found.", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count=count+1
print('There were', count, 'subject lines in', fname)