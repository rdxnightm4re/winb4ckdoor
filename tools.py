import tqdm
import os
import socket

def send_file(filename,buffer_size,server,separator="<SEPARATOR>"):
    print(f"Sending '{filename}'") 
    file_size = os.path.getsize(filename)
    #SEND FILE DATA
    server.send()

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
    file_data = 