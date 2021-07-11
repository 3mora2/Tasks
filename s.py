import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())
s.bind((ip, 8080))
s.listen(5)
client, add = s.accept()
print(client.recv(50000).decode('utf-8'))
while True:
    comment = input('- Enter: ')
    client.send(comment.encode("utf-8"))
