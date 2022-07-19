import socket
import tools
        
def main(): 
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    BUFFER_SIZE = 4096 #KB
    HOSTNAME = socket.gethostname()
    LOCAL_IP = socket.gethostbyname(HOSTNAME)
    PORT = 80 

    #LISTEN FOR CONNECTIONS ON PORT 80
    SERVER.bind((LOCAL_IP,PORT))
    SERVER.listen(1)
    connection,address = SERVER.accept()
    
    print(f"Connection with {address[0]} stablished")
    tools.send_file("test.txt",BUFFER_SIZE,connection)


    
main()