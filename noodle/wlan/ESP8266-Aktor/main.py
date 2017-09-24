#!/usr/bin/python
# -*- coding: utf-8 -*-	

try:
	import uhashlib as hashlib
	import ubinascii
	from ubinascii import hexlify
	import usocket as socket
	import uselect as select
	import utime as time
except ImportError:
	import hashlib
	import binascii
	from binascii import hexlify
	import socket
	import select
	import time


# Config und Vars
CONFIG_FILE = "main_config.cfg"
try:
	with open(CONFIG_FILE) as c:
		print("Lade persistent Config")
		PAIR = c.readline().strip()
		if PAIR != "" and PAIR != "DEFAULTS":
			ID = c.readline().strip()
			SALT = c.readline().strip()
			SEP = c.readline().strip().encode()
		else:
			raise IOError
except IOError:
	print("Keine Config oder Pairing vorhanden (Default)")
	PAIR = False
	ID = 0
	SALT = str(ID)
	SEP = b"%%%"
print(PAIR, ID, SALT, SEP)



class Listener:
	def __init__(self, ip="0.0.0.0", port=8080):
		# Settings
		self.PAIR = PAIR
		self.ID = ID
		self.actions = {}

		# Create Socket
		addr = socket.getaddrinfo(ip, port)[0][-1]
		self.server = socket.socket()
		self.server.setblocking(0)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind(addr)
		self.server.listen(5)

		# Handled Lists
		self.inputs = [self.server]
		self.outputs = []
		self.errors = []

		# Security: Link Funktionen zu Hash
		action_names = ["pair", "unpair", "roll", "rollstatus"]
		action_funcs = [self.pair, self.unpair, self.roll, self.rollstatus]
		for act in range(len(action_names)):
			newKey = hashlib.sha256(str.encode(action_names[act]+SALT)).digest()
			newKey = hexlify(newKey).decode()
			self.actions[newKey] = action_funcs[act]

		print("-- ESP bereit und listening --")


	def run(self):
		while self.inputs:
			# Warten bis eine Liste aktiv wird
			print("...waiting...")
			readable, writable, exceptional = select.select(self.inputs, self.outputs, self.errors)
			# > Inputs
			for sock in readable:
				if sock is self.server:
					# neue eingehende Verbindung
					self.accept_new_connection()
				else:
					# bestehende Verbindun sendet
					data = sock.recv(1024)
					if data:
						# Input bearbeiten / Request in Aktion umwandeln
						print("...processing...")
						req = data.split(SEP)
						req = list(map(lambda x: x.strip().decode(), req))
						try:
							self.actions[req[0]](sock, req[1:])
						except Exception as e:
							print(e)
							sock.send(b"keine action\n")
					else:
						# Hier kommt nichts mehr, Verbindung schließen
						sock.close()
						self.inputs.remove(sock)


	def accept_new_connection(self):
		newsock, (remhost, remport) = self.server.accept()
		if remhost == PAIR or not PAIR:
			self.inputs.append(newsock)
			newsock.send(b"connected\n")
			return (remhost, remport)
		else:
			return False


	def flushConf(self, p=PAIR, i=ID):
		"""Momentane CONFIG (ueber)schreiben"""
		with open(CONFIG_FILE, "w+") as c:
			c.write(self.PAIR)
			c.write("\n")
			c.write(self.ID)
			c.write("\n")
			c.write(SALT)
			c.write("\n")
			c.write(SEP.decode())
			c.write("\n")
		return


	def pair(self, cx, data):
		"""Aktor an eine Node binden (persistent)"""
		print("pairing", data)
		cx.send(b"pairing\n")
		newPair, newID = data
		if len(data) < 2:
			print("zu wenig Argumente !")
			cx.send(b"zu wenig Argumente !\n")
			return
		else:
			self.PAIR = newPair
			self.ID = newID
			self.flushConf()
			print("successfully paired to", newPair, "ID:", newID)
			cx.send(b"successfully paired to "+str.encode(newPair)+b" ID: "+str.encode(newID)+b"\n")
		return


	def unpair(self, cx):
		"""Temporäres Lösen des Pairings für X Sekunden"""
		with open(CONFIG_FILE, "w+") as c:
			c.write("")
		# Mit leerer Config auf Stromtrennung warten
		# Ggf. hier besser etwas mit Schalterinput
		# statt Stromtrennung
		cx.send(b"Waiting 30sec ....")
		#sleep(30)
		sleep(5)
		self.flushConf()
		return

	
	def roll(self, cx, data):
		direction, duration = data[1:3]
		"""Rolladen in eine Richtung bewegen"""
		cx.send(b"Rolle nach "+str.encode(direction)+b" fuer "+str.encode(duration)+b" Sekunden")
		return


	def rollstatus(self, cx):
		"""Position des Rolladens wiedergeben"""
		cx.send(b"Der Rolladen steht gereade irgendwo...")
		return


if __name__ == '__main__':
	server = Listener()
	server.run()