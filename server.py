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
			message = '%s> %s' % (nom, MsgClient)
			print(message)

			# Faire suivre le message à tous les autres clients :
			for cle in conn_client:
				if cle != nom:
					conn_client[cle].send(message.encode('Utf-8'))

		# Fermeture de la connexion
		self.connexion.close() # Couper la connexion coté serveur
		del conn_client[nom] # Supprimer son entrée du dictionnaire
		print('Client %s déconnecté' % nom)
		# Fin du Thread

# Initialisation du serveur - Mise en place du socket :
MainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	MainSocket.bind((host, port))

except socket.error:
	print("[*] La liaison du socket à l'adresse a échoué")
	sys.exit()
print('[*] Serveur prêt, en attente de requêtes...')
MainSocket.listen(5)

# Attente et prise en charge des connexions demandées par les clients :
conn_client = {}
while 1:
	connexion, adresse = MainSocket.accept()
	# Créer un nouvel objet thread pour gérer la connexion :
	th = ThreadClient(connexion)
	th.start()
	# Mémoriser la connexion dans le dictionnaire :
	it = th.getName()
	conn_client[it] = connexion
	print('Client %s connecté, adresse IP %s, port %s' % (it, adresse[0], adresse[1]))
	# Dialogue avec le client :
	msg = 'Vous êtes connecté, envoyez vos messages'
	connexion.send(msg.encode('Utf-8'))
