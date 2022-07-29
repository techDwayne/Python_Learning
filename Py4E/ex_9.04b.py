fname=input('Enter File Name: ')
fhand=open(fname)
emails=dict()
for line in fhand:
    if line.startswith('From '):
        line=line.split()
        email=line[1]
        email=email.split('@')
        domain=email[1]
        emails[domain] = emails.get(domain,0)+1
print(emails)

#loop through the dictionary using a maximum loop to find the most emails from any domain
largest = None
largest_domain = None

for key in emails:
    if largest is None: largest = emails[key]
    if largest < emails[key]:
        largest = emails[key]
        largest_domain=key
        
print(largest_domain,largest)