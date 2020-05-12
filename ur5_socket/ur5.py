import socket
import sys


class DashBoardClient:
    '''
    Connect to the dash board server of UR5.
    Able to:
        1. Run pre-defined programs in the UR5 arm.
        2. Run systematical command, 
                        e.g. power on/off, brake release
    
    More commands are defend here:
    https://s3-eu-west-1.amazonaws.com/ur-support-site/42728/DashCommand.pdf
    '''
    def __init__(self):
        remote_ip = "192.168.56.2"
        port = 29999

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket Created")
        except socket.error as msg:
            print("Failed to create socket. Error code:", str(msg[0]), ", Error message :", msg[1])
        
        s.connect((remote_ip , port))
        print("Socket Connected to", remote_ip, "on port", port)
        self.s = s

        reply = s.recv(1024)
        print(reply)    

    def init_position(self):
        self.send("load /programs/init_position.urp\n")
        self.send("play\n")
        
    def shutdown(self):
        self.send("power off\n")

    def send(self, message):
        try :
        #Set the whole string
            self.s.sendall(bytes(message, encoding = "utf8"))
            # print("Message send successfully")
        except socket.error:
            print("Send failed")
            sys.exit()

        reply = self.s.recv(4096)
        print(reply)