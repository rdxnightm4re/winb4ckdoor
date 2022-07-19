import tqdm
import os
import socket

def send_file(filename,buffer_size,server,separator="<SEPARATOR>"):
    print(f"Sending '{filename}'") 
    file_size = os.path.getsize(filename)
    #SEND FILE DATA
    server.send(f"{filename}{separator}{file_size}".encode())

    progress = tqdm.tqdm(
        range(filesize),
        f"Sending {filename}", 
        unit="B", 
        unit_scale=True, 
        unit_divisor=1024)
    
    with open(filename, "rb") as file:
        while True:
            bytes_read = file.read(buffer_size)
            if not bytes_read:
                break
            server.sendall(bytes_read)
            progress.update(len(bytes_read))


def receive_file(buffer_size,client,separator="<SEPARATOR>",):
    encoding = 'utf-8' 
    file_data = client.recv(buffer_size).decode()
    #ADD TRY CATCH 
    filename,filesize = file_data.split(separator)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    filesize = int(file_size)

    progress = tqdm.tqdm(
        range(filesize),
        f"Sending {filename}", 
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

