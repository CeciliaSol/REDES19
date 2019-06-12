from constants import *

def create_socket():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((RECEIVER_IP, RECEIVER_PORT)) #es para saber donde tiene que escuchar el ip y purta del archivo constantes
	return UDPsocket
	


def extract(packet):
    data=packet.get_data() 
    return data


def deliver_data(message):
	print(message)


def rdt_rcv(sock):
	data=sock.recv(2048)
	paquete=loads(data) #descomprimo con load
	print(paquete)
	return paquete


def close_socket(socket, signal, frame):
	print ("\rCerrando socket")
	socket.close()
	exit(0)


if __name__ == "__main__":
	servidor=create_socket()
	# Creamos el socket "receiver"
	
	# Registramos la senial de salida
	signal.signal(signal.SIGINT, partial(close_socket, servidor))
	# Imprimimos el cartel "Listo para recibir mensajes..."
	print("Listo para recibir mensajes...")
	
	# Iteramos indefinidamente
	while True:
		paquete=rdt_rcv(servidor) # Recibimos un paquete de la red
		data=extract(paquete) # Extraemos los datos
		deliver_data(data) # Entregamos los datos a la capa de aplicacion
		
		
		
		
