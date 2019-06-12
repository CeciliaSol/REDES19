from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_UDPsocket(IP, PORT):
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((IP, PORT))
	return UDPsocket
    
def deliver_data(data): #Saca el encabezado y le spasa los datos a la capa de aplicacion, en este caso pasarselo a la pantalla
    print(data)

def extract(pocket): #por ahora extraer los datos del paquete y devolverlo--CRUSIAL!!! audio para completar
    data=pocket.get_data() 
    return data
    
def rdt_rcv (socket):#de mi socket recibo el paquete y lo devuelve 
    data=socket.recv(2048)

    return data
    
def close_socket(socket):
    socket.close()

def udt_rcv(socket):
    dato=socket.recv(2048)
    paquete=loads(dato)
    return paquete

    
if __name__ == "__main__":
    servidor=create_UDPsocket(RECEIVER_IP, RECEIVER_PORT)
    print('Servidor corriendo')
    while 1:
        paquete=udt_rcv(servidor)
        data=extract(paquete)
        deliver_data(data)
        
    close_socket(servidor)
    
    

    
