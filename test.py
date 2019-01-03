import socket
from multiprocessing import Process

target_host = "infowars.com"
target_port = 80


def test():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_host, target_port))
        client.send(b"GET / HTTP/1.1\r\nHost: infowars.com\r\n\r\n")
        data = client.recv(1024)
        client.close()
        print('Received,', repr(data))


for i in range(0, 3):
    if __name__ == '__main__':
        Process(target=test).start()
