import socket

def send_msg_to_avrcv(msg):
    IP = '192.168.1.100'
    PORT = 8102
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received


# print send_msg_to_avrcv('?ZEP')

# Looks like getting HDZONE Volume
print send_msg_to_avrcv('?V')

# for i in range(256):
#     recv = send_msg_to_avrcv('?RGB{}'.format(i))
#     if not recv.startswith('E0'):
#         print '?RGB{} --> {}'.format(i, recv)

# print send_msg_to_avrcv('?RGB41')