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
def threaded(c,pvideo):
    while True:

        # data received from client
        data = c.recv(1024)

        logging.info("El cliente está en estado: " + str(data.decode("utf-8")))

        print("Cliente "+ str(data.decode("utf-8")))
        options = pvideo
        c.send(options.encode("utf-8"))
        video = pvideo

        data = open(video, "rb")#, encoding="dbcs")
        arch = data.read()
        if not data:
            print('File not found')

            # lock released on exit
            print_lock.release()
            break

        # reverse the given string from client
        #data = data[::-1]
        print("Envio de informacion")
        m = hashlib.sha256()
        m.update(arch)#.encode('dbcs'))
        h = str(m.hexdigest())
        print("Digest enviado: ", m.hexdigest())
        # send back reversed string to client
        c.send(arch)#.encode('dbcs'))
        c.send(m.hexdigest().encode("utf-8"))

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

        # lock acquired by client
        print_lock.acquire()

        print('Connected to client')
        logging.info('Connected to client')
        # Start a new thread and return its identifier
        start_new_thread(threaded, (s,video))
    s.close()


if __name__ == '__main__':
    Main()
