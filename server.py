import socket
import tools
import time 
import concurrent.futures as cf
import threading
import multiprocessing as mp

def wait_for_connections(server,buffer_size): 
    #ACCEPT ANY CONNECTION REQUEST
    connection,address = server.accept()
    print(f"[+] Connection with {address[0]} stablished")
    
    #SEND SECRET MESSAGE (BASE64)
    connection.sendall(b'U295IGVsIGRpb3MgZGUgbGEgZGVzdHJ1Y2Npb24geSBjcmVhY2lvbi4K')
    
    #PROCESS TO RECEIVE DATA (PARALELISM)
    process = mp.Process(
    target=tools.receive_data,
    args=(connection,address,buffer_size,)
    )

    return connection,process


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
    connections = list()
    processes = list()

    while True:
        try:
            with cf.ThreadPoolExecutor() as executor: 
                connection_info = executor.submit(wait_for_connections,SERVER,BUFFER_SIZE)
                connection_info = connection_info.result()

                connection = connection_info[0]
                proccess = connection_info[1]

                connections.append(connection)
                processes.append(process)
                process.start()

        except Exception as exception:
            print("Something went wrong :(")
            print(exception)
            SERVER.close()
            for process in processes:
                print(f"Terminating [{process}]") 
                process.terminate() 
            

main()