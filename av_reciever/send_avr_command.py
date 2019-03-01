import socket

IP = '192.168.1.100'
PORT = 8102

def send_to_avr(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received

# for i in range(256):
#     recv = send_to_avr('?RGB{}'.format(i))
#     if not recv.startswith('E0'):
#         print '?RGB{} --> {}'.format(i, recv)

# print send_to_avr('?RGB41')