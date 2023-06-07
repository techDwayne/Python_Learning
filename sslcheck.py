import requests
import json

def check_ssl(url):
    try:
        req = requests.get(url, verify=True)
        print(url + ' has a valid SSL certificate!')
    except requests.exceptions.SSLError:
        print(url + ' has INVALID SSL certificate!')

with open('urls.json') as json_file:
    json_urls = json.load(json_file)
    for url in json_urls:
        check_ssl(url)
