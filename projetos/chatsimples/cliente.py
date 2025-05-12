import threading
import socket
import tkinter as tk
from tkinter import *
from tkinter import simpledialog

class ChatClient:
    def __init__(self):

        HOST = '127.0.0.1'  # Endereço IP do servidor / localhost no caso de teste
        PORT = 55555  # Porta do servidor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True

        self.nome = simpledialog.askstring("Nome", "Qual o seu nome?", parent=login)
        self.sala = simpledialog.askstring("Sala", "Qual a sala que deseja entrar?", parent=login)

        thread = threading.Thread(target=self.conectar)
        thread.start()
        self.janela()

    def janela(self):
        if not self.janela_carregada:
            self.janela_carregada = True
            self.root = Tk()
            self.root.title("Chat")
            self.root.geometry("800x800")

            self.caixa_texto = Text(self.root)
            self.caixa_texto.place(relx=0.05, rely=0.01, width=600, height=500)
            self.root.mainloop()
            # Entrada de texto para enviar mensagens
            self.envia_mensagem = Entry(self.root)
            self.envia_mensagem.place(relx=0.05, rely=0.8, width=400, height=20)
            # Botão para enviar mensagens
            self.botao_enviar = Button(self.root, text="Enviar", command=self.enviar_mensagem)
            self.botao_enviar.place(relx=0.6, rely=0.8, width=100, height=20)
            # Botão para sair do chat
            self.botao_sair = Button(self.root, text="Sair", command=self.sair_chat)
            self.botao_sair.place(relx=0.8, rely=0.8, width=100, height=20)
            self.root.protocol("WM_DELETE_WINDOW", self.sair_chat)

    def sair_chat(self):
        self.client.destroy()
        self.client.close()


    def conectar(self):
        while True:
            recebido = self.client.recv(1024).decode()
            if recebido == b'SALA':
                self.client.send(self.sala.encode())
                self.client.send(self.nome.encode())
            else:
                try:
                    self.caixa_texto.insert('end', recebido + "\n")
                    self.caixa_texto.see('end')
                except:
                    pass

    def enviar_mensagem(self):
        mensagem = self.envia_mensagem.get()
        self.client.send(mensagem.encode())

chat = ChatClient()