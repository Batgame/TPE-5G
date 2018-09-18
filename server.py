import socket, sys, threading

host = '192.168.1.11'
port= 8080

class ThreadClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn

	def run(self):
		nom = self.getName()
		while 1:
			MsgClient = self.connexion.recv(1024).decode('Utf-8')
			if not MsgClient or MsgClient.upper() == 'FIN':
				break
			message = '%s> %s' (nom, MsgClient)
			print(message)

			for cle in conn_client:
				if cle != nom:
					conn_client[cle].send(message.encode('Utf-8'))

		self.connexion.close()
		del conn_client[nom]
		print('Client %s déconnecté' % nom)

MainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	MainSocket.bind((host, port))

except socket.error:
	print("[*] La liaison du socket à l'adresse a échoué")
	sys.exit()
print('[*] Serveur prêt, en attente de requêtes...')
MainSocket.listen(5)

conn_client = {}
while 1:
	connexion, adresse = MainSocket.accept()
	th_C = ThreadClient(connexion)
	th_C.start()

	it = ThreadClient.getName()
	conn_client[it] = connexion
	print('Client %s connecté, adresse IP %s, port %s' % (it, adresse[0], adresse[1]))

	msg = 'Vous êtes connecté, envoyez vos messages'
	connexion.send(msg.encode('Utf-8'))
