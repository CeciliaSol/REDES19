from constants import *
from packet import *
from constants import *
from network import *

def create_socket(): #crea socket
	servidor = socket(AF_INET, SOCK_DGRAM)
	servidor.bind((RECEPTOR_IP,RECEPTOR_PORT))
	return servidor


def rdt_rcv(red,datos): #recive paquete
	if corrupt(paquete) == NAK:
		udp_send(datos)
	else: 
		datos= socket.recv(2048) 
	 	emisor,paquete = loads(datos) #descomprime


	return (emisor,paquete)
	
def corrupt(pckt):
	if make_pkt(paquete) == pckt:
		return NAK
	else:
		return ACK


def make_pkt(emisor,paquete): #crea el paquete
	paquete = Paquete()
	resultado = calcular_checksum(paquete)
    resultado.set_checksum(resultado)
    return paquete


def udp_send(paquete,emisor): # envia paquete
    datos = dumps(emisor,confirmacion) #Comprimimos los datos
    socket.sendto(dato,(NETWORK_IP,NETWORK_PORT)) # envia dato a la red
	return (datos)


def close_socket(socket, signal, frame):
	print ("\n\rCerrando socket")
	socket.close()
	exit(0)

if __name__ == "__main__":
	servidor= create_socket()# Creamos el socket "receiver"

	while True:
		paquete=rdt_rcv(servidor)# Recibimos un paquete de la red
		if corrupto:
			sndpkt= make_pkt(NAK)
			udp_send(sndpkt)
		else:
			data=extract(paquete)# Extraemos los datos
			deliver_data(data)# Entregamos los datos a la capa de aplicacion		
	close_socket(servidor)
