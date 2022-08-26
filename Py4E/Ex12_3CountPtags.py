import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL to retreive:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve and count paragraph tags
tags = soup('p')
print(tags)
#counts=dict()
#fh=url
#for line in fh:
#    line=line.decode().split()
#    for tag in tags:
#        counts[tag] = counts.get(tag,0) +1
#print(counts)