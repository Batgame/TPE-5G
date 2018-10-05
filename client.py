import socket, sys, threading

host = '192.168.1.x'
port = 8080

class ThreadReceptionMsg(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn # réf. du socket de connexion

	def run(self):
		while 1:
			MsgRecu = self.connexion.recv(1024).decode('Utf-8')
			print('*' + MsgRecu + '*')
			if not MsgRecu or MsgRecu.upper() == "FIN":
				break

		Th_E._stop()
		print('[*] Connexion interrompue')
		self.connexion.close()

class ThreadEmissionMsg(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn

	def run(self):
		while 1:
			MessageEmis = input()
			self.connexion.send(MessageEmis.encode('Utf-8'))

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	connexion.connect((host, port))

except socket.error:
	print('[*] La connexion a échoué')
	sys.exit()

Th_E = ThreadEmissionMsg(connexion)
Th_R = ThreadReceptionMsg(connexion)
Th_R.start()
Th_E.start()
		