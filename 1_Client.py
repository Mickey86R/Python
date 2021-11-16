import socket

IP = "10.0.0.113"
PORT = 7800

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    client.connect((IP, PORT))
    data = client.recv(2048)
    print(data.decode("UTF-16"))
    data = input("::")
    while (data != "quit"):
        client.send(data.encode("UTF-16"))
        data = input("::")
    client.send(data.encode("UTF-16"))
    break

client.close()
