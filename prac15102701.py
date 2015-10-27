import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.douban.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.douban.com\r\nConnection: close\r\n\r\n')

buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)

print(data)

header,html=data.split(b'\r\n\r\n',1)

print(header.decode('utf-8'))
with open('prac15102701.html','wb') as f:
    f.write(html)


s.close()
