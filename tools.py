import tqdm
import os
import socket

def command_line(): 
    pass

def send_file(filename,buffer_size,server,separator="<SEPARATOR>"):
    print(f"Sending '{filename}'") 
    file_size = os.path.getsize(filename)
    #SEND FILE DATA
    server.send(f"{filename}{separator}{file_size}".encode())

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
            server.sendall(bytes_read)
            progress.update(len(bytes_read))


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

