import json
import ssl
import socket

def test_ssl_certificates(json_file):
    with open(json_file) as f:
        urls = json.load(f)
    for url in urls:
        hostname = url.split('/')[2]
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(), server_hostname=hostname)
        conn.connect((hostname, 443))
        cert = conn.getpeercert()
        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']
        issuer = dict(x[0] for x in cert['issuer'])
        issued_by = issuer['commonName']
        print(f"Certificate for {issued_to} issued by {issued_by} is valid.")

json_file = 'github/Python_Learning/urls.json'
test_ssl_certificates(json_file)