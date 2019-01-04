import socket

def send_msg_to_avrcv(msg):
    IP = '192.168.1.100'
    PORT = 8102
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.sendall(msg + '\r')
    received = sock.recv(1024)
    return received


print send_msg_to_avrcv('?P')

########## Get power state #########
#   MAIN        HDZONE      OUTPUT #
#   On          Off         PWR0   #
#   On          On          PWR0   #
#   Off         On          PWR1   #
#   Off         Off         PWR1   #
####################################
# Looks like msg='?P' checks power state of Main Zone. PWR0=On, PWR1=Off

print send_msg_to_avrcv('?HZM')


# Looks like getting HDZONE Volume
print send_msg_to_avrcv('?HZV')

# for i in range(256):
#     recv = send_msg_to_avrcv('?RGB{}'.format(i))
#     if not recv.startswith('E0'):
#         print '?RGB{} --> {}'.format(i, recv)

# print send_msg_to_avrcv('?RGB41')