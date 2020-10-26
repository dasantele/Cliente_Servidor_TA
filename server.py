# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import imageio


print_lock = threading.Lock()


# thread function
def threaded(c):
    print("entre")
    while True:

        # data received from client
        data = c.recv(1024)
        data = imageio.get_reader('imageio:./v1.mp4')
        arch = data
        print(arch)
        if not data:
            print('File not found')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        #data = data[::-1]
        print("envio de info")
        # send back reversed string to client
        c.sendall(arch.encode('utf-8'))

        # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 55000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(1)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()

    '''
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))


from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = 9999
buf =1024
addr = (host,port)
file_name=sys.argv[2]

s.sendto(file_name.encode('utf-8'),addr)

f=open(file_name,"rb")

data = f.read(buf)

s.sendto(data,addr)

while (True):
    if(s.sendto(data,addr)):
        print("sending ...") 
        data = f.read(buf)
    


s.close()
f.close()
    '''