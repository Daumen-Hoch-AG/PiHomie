#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import hashlib
import time
from binascii import hexlify

SALT = "0"
toSend = ""
comm = "rollstatus"
params = b"%%%192.168.178.X%%%1"
dlay = 5

def hashToSend():
	global toSend
	toSend = hashlib.sha256(str.encode(comm+SALT)).digest()
	toSend = hexlify(toSend)+params
	print(toSend)

def main():
	host = ("localhost", 8080)
	s = socket.socket()
	try:
		s.connect(host)
	except Exception:
		print("Unable to connect to {}:{} - ABORT".format(host[0], host[1]))
		return
	print("--- Connected to {} : {}".format(host[0], host[1]))
	print("Sending: {} - {}".format(comm, params))
	print(toSend)
	s.send(toSend)
	print("Wait {}s".format(dlay))
	time.sleep(dlay)
	print("--- Disconnecting")
	s.shutdown(1)
	s.close()
	return


if __name__ == "__main__":
	hashToSend()
	main()