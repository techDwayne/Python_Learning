fname = input('Enter file name: ')
fhandle = open(fname)
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		email = email.split('@')
		domain = email[1]
		emails[domain] = emails.get(domain,0) + 1
print(emails)