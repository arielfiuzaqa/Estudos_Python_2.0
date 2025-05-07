Nome do Projeto: Sistema de Login 
Duração de desenvolvimento cerca de 50 minutos


Descrição do desenvolvimento:
Sistema de Cadastro e Login 
 > Cadastro
    Nome
    Email
    Senha 
        Criptografia na senha mesmo dentro do banco de dados
        Criação de senha Forte, exigir senha Forte
 > Login
    Email
        Não pode se repetir
    Senha
        Criptografia na senha mesmo dentro do banco de dados

> Tratamento de Erros:
    Senha incorreta
    Email incorreto ou inexistente
    Nome não válido (Nomes com caracteres especiais)
    etc.

>> Tecnologias usadas:
 > Python
 > POO 
 > Estrutura MVC
 > Banco de Dados - No caso SQLite com SQLAlchemy
 > ORM - SQLAlchemy