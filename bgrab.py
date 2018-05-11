#!usr/bin/env python

# banner.py
def retBanner(ip, port):
	import socket
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

	sock.connect(ip,port)

	
	sock.send('GET HTTP/1.1 \r\n')
	ret = sock.recv(1024)
	print 'Scanning...'
	print 'Grabbing 192.168.189.159:' + t_port + '[+]' + str(ret)
	return ret
def main():
	portList = [21,22,25,80,110,443]
	for x in range(189,190):
		banner = retBanner(ip, port)
		if banner:
			print '[+]' + ip + ':' + port + '- ' banner
		else :
			banner = 'No banner recieved'
			print '[+]' + ip + ':' + port + '- ' banner 
		
	