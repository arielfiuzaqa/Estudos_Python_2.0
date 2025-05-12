# Fizemos para testar o servidor de forma simples.
import socket
import threading

HOST = '127.0.0.1'  # Endereço IP do servidor / localhost no caso de teste
PORT = 55555  # Porta do servidor

# Cria um socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))  # Associa o socket ao endereço e porta

mensagem = client.recv(1024)  # Recebe a mensagem do servidor
if mensagem == b'SALA':
    client.send(b'Games')
    client.send(b'Ariel')
