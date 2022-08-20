
import socket

msock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msock.connect(('data.pr4e.org', 443))
cmd = 'GET https://data.pr4e.org/romeo.txt \r\n\r\n'.encode()
print(cmd)
msock.send(cmd)

while True:
    data=msock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
msock.close