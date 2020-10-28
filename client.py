'''
import socket 
 
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 55000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    
    # connect to server on local computer
    preparado = "Preparado"
    s.sendto(preparado.encode("utf-8"), (host, port))
    #if(s.connect((host,port))==0): 
    print("Conectado con el servidor")
    print("Preparado para recibir datos del servidor")
    
    # message you send to server 
    message = "prueba"
    while True: 

        # message sent to server 
        #s.send(message.encode('ascii')) 
  
        # messaga received from server 
        data = s.recvfrom(1024) 
  
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
import socket
import sys
import select
import hashlib
from time import time


host="127.0.0.1"
port = 55000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s.bind((host,port))
f = open("clienteRecibido.txt", 'wb')
dataTot=b''
while True:
    hashmd5 = hashlib.md5()   
    addr = (host,port)
    buf=2040
    preparado = "Preparado"
    s.sendto(preparado.encode("utf-8"), (host, port))
    tiempo_inicial = time()

    print("Conectado con el servidor")
    print("Preparado para recibir datos del servidor")
    
   

    data = s.recvfrom(buf)
    #f.write(data) 
    #dataTot+=data
    print ("Received %s bytes from:" %(len(data)),addr)
    hashh = s.recvfrom(buf)
    #logging.info("Recibio datos: video "+resp+ " de tamano " + str(round(Path(video).stat().st_size/(1024*1024), 2))+" MB")
    #logging.info("Recibio su hash: "+ str(hashh.decode('utf-8')) )
    hashRecibido = hashh
    print("Hash recibido: " + str(hashRecibido))
    arch = data

        #.decode('dbcs')
        # print the received message 
        # here it would be a reverse of sent message 
    #print('Received file from the server :'+ resp + "de tamaño" + str(round(Path(video).stat().st_size/(1024*1024), 2))+" MB")#,str(data.decode('ANSI'))) 
    #m = hashlib.sha256()
    #m.update(dataTot)#.encode('dbcs'))
    #h = str(m.hexdigest())
    print("Recibido: "+ hashRecibido[0].decode() )
    #print("Calculado: "+h)
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    #logging.info("Tiempo que se tardo en enviar los archivos: "+ str(round(tiempo_ejecucion, 2))+ " ms")
        
    print("tiempo de operación: "+ str(tiempo_ejecucion))
    #print("Digest calculado: ", m.hexdigest())

    if(True):
        s.sendto("File checked sucessfully".encode('utf-8'),addr)   
    else:
        s.sendto("File sent with problems".encode('utf-8'),addr)
        s.close()
    break
s.close()


    
print ("Done")
