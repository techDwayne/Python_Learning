fname=input('Enter File Name: ')
fhand=open(fname)
emails=dict()

for line in fhand:
    if line.startswith('From: '):
        line=line.split()
        email=line[1]
        print(email)
        email=email.split('@')
        domain=email[1]
        emails[domain] = emails.get(domain,0)+1
print(emails)
