# import socket programming library
import socket
import hashlib
# import thread module
from _thread import *
import threading
import os, platform, logging

    
if platform.platform().startswith('Cliente-Servidor-Infracom'):
        fichero_log = os.path.join('archivoServidor.log')
else:
        fichero_log = os.path.join('archivoServidor.log')

print('Archivo Log en ', fichero_log)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename=fichero_log,
                    filemode='a', ) 

print_lock = threading.Lock()


# thread function
def threaded(c,pvideo,addr):
    while True:

        options = pvideo
        c.sendto(options.encode(),addr)
        video = pvideo

        m = hashlib.sha256()
        data = open(video, "rb")
        arch = data.read(2040)
        hashd =data.read()
        m.update(hashd)
        if not data:
            print('File not found')
            # lock released on exit
            print_lock.release()
            break

        bytesEfectivamenteEnviados = 0
        while(arch):
            bytesEnviados = c.sendto(arch,addr)
            if(bytesEnviados):
                bytesEfectivamenteEnviados+=bytesEnviados
                arch = data.read(2040)

        data.close()

        print("--> Envio de informacion")
        print("Digest enviado: ", m.hexdigest())
        bytesEnviadosHash = c.sendto(m.hexdigest().encode(),addr)


        logging.info('SERVER cliente %s:%s bytes enviados en total %s',
                 addr[0], addr[1], bytesEfectivamenteEnviados + bytesEnviadosHash)


        # lock released on exit
        print_lock.release()
        break
    # connection closed
    c.close()


def Main():
    host = ""#socket.gethostname()

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 55000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("Server binded to port", port)
    addr = (host,port)
    # put the socket into listening mode
    print("Server is listening")
    resp = input("Ingrese que archivo desea que se envie a los clientes (1 o 2) ")
    print(resp)
    if resp == '1':
        video = "./video.mp4"
    else:
        video = "./video2.mp4"

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.recvfrom(2**15)
        print_lock.acquire()
        print(c)
        print('Connected to :', addr[0], ':', addr[1])
        logging.info('Connected to : ,'+ str(addr[0]) +' , : , ' + str(addr[1]))
        # Start a new thread and return its identifier
        data = c
        logging.info("El cliente está en estado: " + str(data.decode("utf-8")))

        print("Cliente "+ str(data.decode("utf-8")))
        start_new_thread(threaded, (s,video, addr))
        
    s.close()


if __name__ == '__main__':
    Main()
