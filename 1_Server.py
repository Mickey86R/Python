import socket

IP = "10.0.0.113"
PORT = 7800

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

server.listen()

while True:
    sock, addr = server.accept()
    print(f"К серверу подключился {sock}")
    sock.send("Welcome to Server!".encode("UTF-16"))
    data = sock.recv(2048)
    while (data.decode("UTF-16") != "quit"):
        print(data.decode("UTF-16"))
        data = sock.recv(2048)
    print(data.decode("UTF-16") + "qweqwe")
    break

server.close()
print("Сервер закрыт")
