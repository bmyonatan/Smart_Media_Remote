import socket

def send_msg_to_avrcv(msg):
    IP = '192.168.1.100'
    PORT = 8102
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received


print send_msg_to_avrcv('?RGD')

#### Get power state ###
#   MAIN        HDZONE      OUTPUT #
#   On          Off         PWR0   #
#   On          On          PWR0   #
#   Off         On          PWR1


print send_msg_to_avrcv('?HZV')