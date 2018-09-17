import socket, sys

host = '192.168.1.11'
port = '8080'

MainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	MainSocket.connect((host, port))

except socket.error:
	print('[*] La connexion a échoué')
	sys.exit()
print('[*] Connexion établie avec le serveur')

MsgServeur = MainSocket.recv(1024).decode('Utf-8')

while 1:
	if MsgServeur.upper() == "FIN" or MsgServeur == "":
		break
	print('Serveur> ', MsgServeur)
	MsgClient = input('Client> ')
	MainSocket.send(MsgClient.encode('Utf-8'))
	MsgServeur = MainSocket.recv(1024).decode('Utf-8')

print('[*] Connexion interrompue')
MainSocket.close()