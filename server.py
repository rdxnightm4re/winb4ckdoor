import socket
import tools
import time 
import threading

def wait_for_connections(server): 
    while True:
        connection = server.accept()
        print(f"[+] Connection with {connection[0]} stablished")
        
        connection.sendall(b'U295IGVsIGRpb3MgZGUgbGEgZGVzdHJ1Y2Npb24geSBjcmVhY2lvbi4K')
        
        return connection


def main(): 
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    BUFFER_SIZE = 4096 #KB
    HOSTNAME = socket.gethostname()
    LOCAL_IP = tools.get_local_ip(SERVER,HOSTNAME)
    PORT = 8080 

    #LISTEN FOR CONNECTIONS ON PORT 80
    print(f"[+] Listening for connections on {LOCAL_IP}:{PORT}")
    SERVER.bind((LOCAL_IP,PORT))
    SERVER.listen(1)
    
    threading.Thread()
    connections = wait_for_connections(SERVER,BUFFER_SIZE)
    # tools.send_file("config.json",BUFFER_SIZE,connection)

main()