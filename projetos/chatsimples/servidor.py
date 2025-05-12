import socket
import threading

HOST = '127.0.0.1'  # Endereço IP do servidor / localhost no caso de teste
PORT = 55555  # Porta do servidor

# Cria um socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))  # Associa o socket ao endereço e porta
server.listen()  # Escuta por conexões
print(f'Servidor iniciado em {HOST}:{PORT}')    

salas = {}  # Dicionário para armazenar as salas

def broadcast(mensagem, sala):
    # Envia a mensagem para todos os clientes na sala
    for cliente in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        cliente.send(mensagem)

def enviar_mensagem(nome, sala, cliente):
    while True:
        mensagem = cliente.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n'
        broadcast(mensagem.encode(), sala)

while True:
    client, addr = server.accept()  # Aceita uma conexão
    print(f'Conexão recebida de {addr}')  # Exibe o endereço do cliente
    print(client)  # Exibe o socket do cliente

    client.send(b'SALA') 
    sala = client.recv(1024).decode()  # Recebe o nome da sala
    nome = client.recv(1024).decode()  # Recebe o nome do cliente
    print(f'Cliente {nome} entrou na sala {sala}')  # Exibe o nome do cliente e da sala
    # Adiciona o cliente à sala
    # Verifica se a sala já existe, se não existir, cria uma nova sala
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)  # Adiciona o cliente à sala
    print(f'Clientes na sala {salas}: {salas[sala]}')  # Exibe os clientes na sala
    broadcast(f'{nome} entrou na sala {sala}'.encode(), sala)  # Envia mensagem para todos os clientes na sala
    thread = threading.Thread(target=enviar_mensagem, args=(nome, sala, client))  # Cria uma thread para enviar mensagens
    thread.start()  # Inicia a thread