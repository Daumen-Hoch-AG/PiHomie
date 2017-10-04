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
			ID = int(c.readline().strip())
			SALT = c.readline().strip()
			SEP = c.readline().strip().encode()
		else:
			raise OSError
except OSError:
	print("Keine Config oder Pairing vorhanden (Default)")
	PAIR = False
	ID = 0
	SALT = str(ID)
	SEP = b"%%%"

print("> Config:", "PAIR ID SALT SEP")
print(PAIR, ID, SALT, SEP)



class Listener:
	def __init__(self, ip="0.0.0.0", port=8080):
		# von der Klasse editierbare Settings
		self.PAIR = PAIR
		self.ID = ID
		self.actions = {}
		# Flags
		self.timer = 0 # (< statt int besser date.time verwenden)
		self.interrupted = False
		self.cache = ""

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
		print("\n> Hashes:")
		self.action_names = ["pair", "unpair", "roll", "rollstatus"]
		action_funcs = [self.pair, self.unpair, self.roll, self.rollstatus]
		for act in range(len(self.action_names)):
			newKey = hashlib.sha256(str.encode(self.action_names[act]+SALT)).digest()
			newKey = hexlify(newKey).decode()
			self.actions[newKey] = action_funcs[act]
			print(newKey, "\t", self.action_names[act])

		print("\n-- ESP bereit und listening --")


	def run(self):
		while True:
			# Handle Interrupt-Flags
			if self.interrupted:
				print("Interrupted !")
				req = self.interrupted.split(SEP)
				req = list(map(lambda x: x.strip(), req))
				self.actions[req[0]](self.server, req[1:])
				self.interrupted = False
			# Warten bis eine Liste aktiv wird
			print("...waiting...")
			readable, writable, exceptional = select.select(self.inputs, self.outputs, self.errors)
			# > Inputs
			for sock in readable:
				if sock is self.server:
					# neue eingehende Verbindung
					r = self.accept_new_connection()
					if r:
						print("Client", r[0], ":", r[1], "connected")

				else:
					# bestehende Verbindung sendet
					try:
						# versuche zu Empfangen
						data = sock.recv(1024)
						if data:
							# Input parsen
							print("...processing...")
							try:
								req = data.split(SEP)
								req = list(map(lambda x: x.strip().decode(), req))
								msg = self.actions[req[0]](req[1:])
							except Exception as e:
								print(e.__class__.__name__, ":", e)
								msg = b"keine action\n"
							sock.send(msg)
						else:
							raise Exception
					except Exception as e:
						# Hier kommt nichts mehr, Verbindung schließen
						print("Connection closed:", sock)
						sock.close()
						self.inputs.remove(sock)

			# Outputs / Flags
			for timer in writable:
				if type(timer) == int and self.timer > 0:
					# Action Listener
					if self.timer-1 > 0:
						# weitere Sekunde laufen lassen
						time.sleep(1)
						self.timer -= 1
						print(self.action_names[timer], self.timer, "Sek. left")
					else:
						# Action beenden
						print("Stopping...")
						self.stopAction(timer)



	def accept_new_connection(self):
		newsock, (remhost, remport) = self.server.accept()
		if remhost == PAIR or not PAIR:
			self.inputs.append(newsock)
			newsock.send(b"connected\n")
			return (remhost, remport)
		else:
			return False


	def flushConf(self):
		"""Momentane CONFIG (ueber)schreiben"""
		with open(CONFIG_FILE, "w+") as c:
			if not self.PAIR:
				c.write(self.cache)
			else:
				c.write(self.PAIR)
				c.write("\n")
				c.write(self.ID)
				c.write("\n")
				c.write(SALT)
				c.write("\n")
				c.write(SEP.decode())
				c.write("\n")


	def stopAction(self, timer):
		"""Stoppt Bewegung und resettet Timer"""
		toStop = self.action_names[timer]
		if toStop == "roll":
			# <Stoppen triggern/schalten>
			pass
		elif toStop == "unpair":
			# Unpairing verlassen
			self.flushConf()
		self.timer = 0
		self.outputs.remove(timer)
		return
		return


	def pair(self, data):
		"""Aktor an eine Node binden (persistent)"""
		print("-pairing", data)
		newPair, newID = data
		if len(data) < 2:
			print("zu wenig Argumente !")
			return b"zu wenig Argumente !\n"
		else:
			self.PAIR = newPair
			self.ID = newID
			self.flushConf()
			print("erfolgreich gepaired zu", newPair, "ID:", newID)
			return b"erfolgreich gepaired zu "+str.encode(newPair)+b" ID: "+str.encode(newID)+b"\n"


	def unpair(self, data):
		"""Temporäres Lösen des Pairings für X Sekunden"""
		print("-unpair")
		with open(CONFIG_FILE, "r") as c:
			# Caching
			self.cache = c.read()
		with open(CONFIG_FILE, "w") as c:
			# Löschen
			c.write("")
		# Mit leerer Config auf Stromtrennung warten
		# Ggf. hier besser etwas mit Schalterinput
		# statt Stromtrennung
		self.timer = 30
		self.outputs = [self.action_names.index('unpair')]
		return b"Warte 30 Seks mit leerer Config...."


	def roll(self, data):
		"""Rolladen in eine Richtung bewegen"""
		try:
			direction, duration = data[0:2]
			# <Rollen triggern/schalten>
			self.timer = int(duration)
			self.outputs = [self.action_names.index('roll')]
			print("-rollen nach", direction, "fuer", duration)
			return b"Rolle nach "+str.encode(direction)+b" fuer "+str.encode(duration)+b" Sekunden"
		except Exception:
			return b"falsche Argumente"


	def rollstatus(self, data):
		"""Position des Rolladens wiedergeben"""
		print("-rollstatus")
		return b"Der Rolladen steht gereade irgendwo..."


if __name__ == '__main__':
	server = Listener()
	server.run()