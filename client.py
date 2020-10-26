'''
import socket 
 
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 55000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    if(s.connect((host,port))==0): 
        print("Conectado con el servidor")
        print("Preparado para recibir datos del servidor")
    
    # message you send to server 
    message = "prueba"
    while True: 

        # message sent to server 
        s.send(message.encode('ascii')) 
  
        # messaga received from server 
        data = s.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from the server :',str(data.decode('utf-8'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'

try:

    print("Conectado con el servidor")
    print("Preparado para recibir datos del servidor")
    
    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)
 
    
    # Receive response
    print('Esperando...')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

'''
from socket import *
import sys
import select
import hashlib

host="0.0.0.0"
port = 9999

s = socket(AF_INET,SOCK_DGRAM)

s.bind((host,port))

while True:
    hashmd5 = hashlib.md5()   
    addr = (host,port)
    buf=2040
    print("Conectado con el servidor")
    print("Preparado para recibir datos del servidor")
    data,addr = s.recvfrom(buf)
    print ("Received %s bytes from:" %(len(data)),addr)
    print(data)
    print("sending ack to",addr)
    
    if(True):
        s.sendto("File checked sucessfully".encode('utf-8'),addr)   
    else:
        s.sendto("File sent with problems".encode('utf-8'),addr)
    s.close()
    break

if(s.timeout):
    s.close()
    
print ("Done")
