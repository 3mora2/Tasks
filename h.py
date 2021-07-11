import socket
ip = socket.gethostbyname(socket.gethostname())
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 8080))
    print('done')
    s.send("the client user is User".encode("utf-8"))
    while True:
        command = s.recv(5000).decode("utf-8")
        print(command)
except socket.error as e:
    print(e)
