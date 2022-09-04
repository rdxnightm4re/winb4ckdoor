import socket
import tools
import time 
import concurrent.futures as cf
import multiprocessing as mp

def handle_connections(server,buffer_size,active_connections): 
    #ACCEPT ANY CONNECTION REQUEST
    connection,address = server.accept()

    #IF LOCAL IP IN ACTIVE CONNECTIONS DENY
    if address[0] in active_connections.keys():
        active_connections[address[0]][1].terminate()
        del active_connections[address[0]]
        print(f"[+] Connection with {address[0]} restablished")
    else:
        print(f"[+] New connection with {address[0]}")

    #SEND SECRET MESSAGE (BASE64)
    #connection.sendall(b'U295IGVsIGRpb3MgZGUgbGEgZGVzdHJ1Y2Npb24geSBjcmVhY2lvbi4K')

    #PROCESS TO RECEIVE DATA (PARALELISM)
    process = mp.Process(
    target=tools.receive_data,
    args=(connection,address[0],buffer_size,)
    )

    return connection,address,process


def main(): 
    #SERVER DATA
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    BUFFER_SIZE = 4096 #KB
    HOSTNAME = socket.gethostname()
    LOCAL_IP = tools.get_local_ip(SERVER,HOSTNAME)
    PORT = 8080 

    #LISTEN FOR CONNECTIONS ON PORT 80
    print(f"[+] Listening for connections on {LOCAL_IP}:{PORT}")
    SERVER.bind((LOCAL_IP,PORT))
    SERVER.listen(1)

    #WAIT FOR CONNECTIONS IN A DIFFERENT PROCESS
    active_connections = dict()

    while True:
        connections_count = len(active_connections)

        try:
            with cf.ThreadPoolExecutor() as executor: 
                connection_info = executor.submit(
                handle_connections,
                SERVER,BUFFER_SIZE,
                active_connections
                )
                
                connection_info = connection_info.result()   

                if connection_info:
                    #GATHER CONNECTION INFO
                    connection = connection_info[0]
                    address = connection_info[1]         
                    process = connection_info[2]

                    #ADD TO ACTIVE CONNECTIONS DICT
                    active_connections[address] = [connection,process]

                    #START RECEIVING DATA IN ANOTHER PROCESS
                    process.start()

        except Exception as exception:
            print("Something went wrong :(")
            print(exception)
            SERVER.close()
            for process in processes:
                print(f"Terminating [{process}]") 
                process.terminate() 
            
if __name__ == "__main__":
    main()
