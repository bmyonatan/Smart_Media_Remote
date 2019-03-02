import socket

IP = '192.168.1.100'
PORT = 8102


def send_to_avr(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received
