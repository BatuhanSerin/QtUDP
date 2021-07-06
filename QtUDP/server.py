
import socket
class Server():
    
    def __init__(self,label):
        
        self.label=label
        self.act()
        
    def act(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

        host = socket.gethostname()		        
        port = 60000			                
        
        s.bind((host,port))
        
        while True:
            print ("Waiting for client...")
            self.label.setText("Waiting for client...")
            data,addr = s.recvfrom(1024)	        
            print ("Received Messages:",data," from",addr)
            self.label.setText("Received Messages:",data," from",addr)

        
