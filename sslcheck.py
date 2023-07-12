import json
import requests

def check_ssl(url):
    try:
        response = requests.get(url,timeout=2)
        if response.ok:
            return response
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def check_urls(json_file):
    with open(json_file, 'r') as file:
        urls = json.load(file)

    for url in urls:
        response = check_ssl(url)
        if response is not None:
            if response.status_code == 200:
                print(f"{url} - Valid SSL certificate")
            else:
                print(f"{url} - Invalid SSL certificate")
        else:
            print(f"{url} - Unable to connect")

json_file_path = '/home/lds/github/Python_Learning/urls.json'
check_urls(json_file_path)
