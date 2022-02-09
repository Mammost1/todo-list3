from socket import *
while True:
    HOST = str(input('Please input server ip address :'))
    PORT = 4444
    
    BUFFER_SIZE = 1024 
    ADDRESS = (HOST,PORT)
    
    server = socket(AF_INET,SOCK_STREAM)
    #---------------------------------castom
    try:
        server.connect(ADDRESS)
        messageFromServer = bytes.decode(server.recv(BUFFER_SIZE))
        print(messageFromServer)
        while True:
            message = input(' > ')
            try:
                server.send(str.encode(message))
            except ConnectionResetError:
                print("Server disconnected")
                break
            if not message:
                break
            reply = bytes.decode(server.recv(BUFFER_SIZE))
            if not reply:
                print("Server disconnected")
                break
            print("Server said : "+ reply)
            
        server.close()
        print("Left chat")
    except ConnectionRefusedError and TimeoutError:
        print("Server not response")
    



