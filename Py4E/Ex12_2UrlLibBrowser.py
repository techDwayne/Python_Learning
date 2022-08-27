import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

counts=dict()
fh=urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in fh:
    words=line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) +1
print(counts)

fhnd=urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fhnd:
    print(line.decode().strip())