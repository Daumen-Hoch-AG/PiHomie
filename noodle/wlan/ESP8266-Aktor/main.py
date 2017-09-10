# Diese Datei wird immer nach der boot.py ausgefuehrt

import socket
from time import sleep

# Config und Vars
HTTP_HEADER = "HTTP/1.1 200 OK \n\n"
CONFIG_FILE = "main_config.cfg"
try:
	with open(CONFIG_FILE) as c:
		print("Lade persistent Config")
		PAIR = c.readline().strip()
		if PAIR == "":
			# Empty: Defaults
			PAIR = False
			ID = 0
		else:
			ID = c.readline().strip()
		print("PAIR:", PAIR)
		print("ID:", ID)
except IOError:
	print("Keine Config vorhanden (Default)")
	PAIR = False
	ID = 0




def pair(cx, newPair, newID):
	"""Aktor an eine Node binden (persistent)"""
	if not newID:
		print("missing newID - no changes made !")
		cx.write("missing newID - no changes made !")
		return
	else:
		PAIR = newPair
		ID = newID
		flushConf(PAIR, ID)
		print("successfully paired to", newPair, "ID:", newID)
		cx.write("successfully paired to "+newPair+" ID: "+newID)
	return


def unpair(cx):
	"""Temporäres Lösen des Pairings für X Sekunden"""
	with open(CONFIG_FILE, "w+") as c:
		c.write("")
	# Mit leerer Config auf Stromtrennung warten
	# Ggf. hier besser etwas mit Schalterinput
	# statt Stromtrennung
	cx.write("Waiting 30sec ....")
	#sleep(30)
	sleep(5)
	flushConf()
	return


def roll(cx, direction, duration):
	"""Rolladen in eine Richtung bewegen"""
	cx.write("Rolle nach "+str(direction)+" fuer "+str(duration)+" Sekunden")
	return


def parsePayload(payload):
	"""POST Daten in Dictionary parsen"""
	liste = payload.decode().split("&")
	d = {x.split("=")[0]: x.split("=")[1] for x in liste}
	return d


def flushConf(p=PAIR, i=ID):
	"""Momentane CONFIG (ueber)schreiben"""
	with open(CONFIG_FILE, "w+") as c:
		c.write(p)
		c.write("\n")
		c.write(i)
		c.write("\n")
	return


def startListening(ip="0.0.0.0", port=8080):
	addr = socket.getaddrinfo(ip, port)[0][-1]
	
	# Start Socket
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # IP reusabillity
	s.bind(addr)
	s.listen(5)
	print("Listening on", ip, ":", port)
	
	while True:
		# Accept Connections
		conn, cl_addr = s.accept()
		print("--> incomming request from", cl_addr[0], "Port", cl_addr[1])

		# nur mit PAIR kommunizieren
		if not PAIR or cl_addr[0] == PAIR:
			conn.write(HTTP_HEADER)

			# Read Requests
			header = conn.readline()
			req = header.split(b" ")[0]
			payload = b""
			print("Request:", header)
			while True:
				header = conn.readline()
				if header == b"" or header == b"\r\n":
					if req == b'POST':
						payload = conn.recv(4096)
					break

			if req == b'POST':
				# Handle Request
				print("Payload:", len(payload))
				p = parsePayload(payload)
				print(p)
				if "action" in p:

					if p["action"] == "pair":
						if not PAIR:
							pair(conn, cl_addr[0], p.get("newid", False))
						else:
							conn.write("device already paired to "+PAIR)

					elif p["action"] == "unpair":
						unpair(conn)

					elif p["action"] == "roll":
						roll(conn, p.get("direction", 1), p.get("duration", 0))

					else:
						conn.write("no action specified")

				else:
					conn.write("Pong !")

			if not PAIR:
				conn.write("\nWARNING: This device is not paired yet !")

		else:
			print(cl_addr, "is not my PAIR", PAIR)

		# Disconnect
		conn.close()
		print(cl_addr[0], "disconnected")
		print()


# Start App
startListening()
