# Diese Datei wird immer nach der boot.py ausgefuehrt

import socket


# Responses
CONTENT = {
	"OK" : """HTTP/1.0 200 OK

Thanks for trying :)
""",
}

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
		# Handle Requests
		while True:
			req = conn.readline()
			if req == b"" or req == b"\r\n":
				break
			print(req)
	
		# Sende etwas nach dem Request ?
		conn.write(CONTENT["OK"])

		# Disconnect
		conn.close()
		print(cl_addr[0], "disconnected")
		print()


# Start App
startListening()
