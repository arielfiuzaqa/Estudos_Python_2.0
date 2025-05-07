import socket as sck

HOST = 'localhost'  # Endereço IP do servidor
PORT = 8000  # Porta do servidor

sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # Cria um socket TCP
sock.bind((HOST, PORT))  # Associa o socket ao endereço e porta
sock.listen(2)  # Escuta por conexões

while True:
    novoSock, _ = sock.accept()  # Aceita uma nova conexão
    mensagem = novoSock.recv(1024).decode()  # Recebe a mensagem do cliente em binário 
    print(f"Mensagem recebida: {mensagem}")  # Decodifica a mensagem e imprime
    novoSock.send(b"Ok")  # Envia uma resposta para o cliente