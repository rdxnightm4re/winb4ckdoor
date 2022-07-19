import socket
import os
import time
import tqdm
import tools 


def main():
    CLIENT=socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
        )
    
    #LOCAL DATA
    HOSTNAME = socket.gethostname()
    LOCAL_IP = socket.gethostbyname(HOSTNAME)
    BUFFER_SIZE = 4096 #KB

    #SERVER DATA 
    SERVER_IP = "192.168.1.74"
    SERVER_PORT = 80
    
    CLIENT.settimeout(20)
    CLIENT.connect((SERVER_IP,SERVER_PORT))    
    print(f"Connection with {SERVER_IP} on {SERVER_PORT}")

main()