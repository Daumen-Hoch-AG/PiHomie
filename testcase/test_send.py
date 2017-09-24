#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import hashlib
import time
from binascii import hexlify

SALT = "0"
toSend = ""
params = b"%%%192.168.178.X%%%1"

def hashToSend():
	global toSend
	#toSend = hashlib.sha256(str.encode(action_names[act]+SALT)).digest()
	#toSend = hexlify(toSend).decode()
	toSend = hashlib.sha256(str.encode("rollstatus"+SALT)).digest()
	toSend = hexlify(toSend)+params
	print(toSend)

def main():
	host = ("localhost", 8080)
	s = socket.socket()
	try:
		s.connect(host)
	except Exception:
		print("Unable to connect ! - ABORT")
		return
	print("Connected to {} : {}".format(host[0], host[1]))
	print("Sending:")
	print(toSend)
	s.send(toSend)
	time.sleep(5)
	return


if __name__ == "__main__":
	hashToSend()
	main()