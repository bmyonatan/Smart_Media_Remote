import socket
import time

IP = '192.168.1.100'
PORT = 8102

def send_to_avr(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received

for i in range(10, 256):
    query = '?RGB{:02}'.format(i)
    print query
    recv = send_to_avr(query)
    if not recv.startswith('E0'):
        print '?RGB{} --> {}'.format(i, recv)
    # time.sleep(0.4)
# print send_to_avr('?RGB41')