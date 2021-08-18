#practice ex_08_04
fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    email=words[1]
   # print(email)
    host=email.split('@')
    print(host[1])