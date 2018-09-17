import socket, sys

host = '192.168.1.11'
port= '8080'
counter = 0

MainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	MainSocket.bind((host, port)) #Liaison du socket à l'adresse et au port

except socket.error:
	print("[*] La liaison du socket à l'adresse à échoué.")
	sys.exit

while 1:
	print('[*] Serveur prêt, en attente de requêtes...')
	MainSocket.listen(2) #Attente d'une connexion entrante

	connexion, adresse = MainSocket.accept() #Connexion entrante accepté
	counter +=1
	print('[*] Client connecté, adresse IP %s, port %s' % (adresse[0], adresse[1]))

	MsgServeur = "Vous êtes connecté au serveur Batgame. Envoyer vos messages."
	connexion.send(MsgServeur.encode('Utf-8')) #Le message de bienvenue est envoyé au client (encodé en UTF8)
	MsgClient = connexion.recv(1024).decode('Utf-8') #Si reception d'un message du client, le decoder
	while 1:
		print('Client> 'MsgClient)
		if MsgClient.upper() == "FIN" or MsgClient == "":
			break
		MsgServeur = input('Serveur> ')
		connexion.send(MsgServeur.encode('Utf-8'))
		MsgClient = connexion.recv(1024).decode('Utf-8')

	connexion.send('Fin'.encode('Utf-8'))
	print('[*] Connexion interrompue.')
	connexion.close()

