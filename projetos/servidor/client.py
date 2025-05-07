import socket as sck

HOST = 'localhost'  # Endereço IP do servidor
PORT = 8000  # Porta do servidor

sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # Cria um socket TCP
sock.connect((HOST, PORT))  # Conecta ao servidor
mensagem = input('Digite sua mensagem: ').encode()  # Mensagem a ser enviada

sock.send(mensagem)  # Envia a mensagem para o servidor
print(f"Mensagem enviada: {mensagem}")  # Imprime a mensagem 

confimacao = sock.recv(1024)  # Recebe a confirmação do servidor
if confimacao == b"Ok":  # Verifica se a confirmação é "Ok"
    print(f"Confirmação recebida: {confimacao.decode('utf-8')}")  # Decodifica a confirmação e imprime