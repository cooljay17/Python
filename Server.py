#server
import socket

s = socket.socket()
port = 8080
s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send(b'Client and server are connected..Yay!!!')    
    c.close()