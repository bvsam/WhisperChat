#User Client side

#Standard procedure
#Run the server.py on server
#User run this file
#Register  
#Enter the username with a ‘#’ prefix. Example: #alice
#Send the message to a user by following the format @username:message. Example: @bob:Hello, Bob! This is alice
#Repeat step 2 for other users. (Maximum 5 users is allowed with server configuration i.e. server_socket.listen(5)
#Run reciever before use this script function

import socket
import encryption
import chatClientReciever


client_socket = socket.socket()
port = 12345
client_socket.connect(('127.0.0.1',port))




#Input message_body, userneame.
#Body message -> encode -> encryption -> sending
def send_message(send_msg,recipient):
    recipient = recipient.strip()
    message = message.encode('utf-8')
    public_key = encryption.read_public_key(recipient)
    encrypt_message = encryption.encrypt(message,public_key)
    send_msg = "@"+recipient+":"+encrypt_message
    client_socket.send(send_msg.encode('utf-8'))





