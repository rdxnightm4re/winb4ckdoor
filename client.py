import socket
import tools 
import threading



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
    SERVER_IP = "192.168.1.70"
    SERVER_PORT = 8080
    
    #CLIENT.settimeout(20)
    
    print(f"[+] Stablishing connection with {SERVER_IP} on port {SERVER_PORT}")

    try:
        CLIENT.connect((SERVER_IP,SERVER_PORT))    
    except TimeoutError:
        print(f"[-] Connection timeout with {SERVER_IP}")
        CLIENT.close()
        print(f"[+] Trying again...")
        main()

    print(f"[+] Connection with {SERVER_IP} on port {SERVER_PORT}")
    #tools.receive_file(BUFFER_SIZE,CLIENT)

    system_details = tools.get_system_info().encode()
    CLIENT.send(system_details)

    while True:
        data = CLIENT.recv(BUFFER_SIZE)
        print(data)


    CLIENT.close()
    print(f"[-] Connection with {SERVER_IP} closed.")

try:
    main()
except KeyboardInterrupt:
    print("Bye uwuwu") 
