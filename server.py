import socket
import tools
import time 

def main(): 
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    BUFFER_SIZE = 4096 #KB
    HOSTNAME = socket.gethostname()
    LOCAL_IP = socket.gethostbyname(HOSTNAME)
    PORT = 8080 

    #LISTEN FOR CONNECTIONS ON PORT 80
    print(f"Listening for connections on {LOCAL_IP}:{PORT}")
    SERVER.bind((LOCAL_IP,PORT))
    SERVER.listen(1)
    connection,address = SERVER.accept()
    
    print(f"Connection with {address[0]} stablished")
    tools.send_file("server.py",BUFFER_SIZE,connection)


    
main()