PROJETO II - HAPVIDA NDI - BANCO DE DADOS DE PESSOAS DA TI

🧠 Objetivo
Criar um sistema de cadastro, visualização e gerenciamento de colaboradores da área de TI do Hapvida NDI com estrutura organizacional (Gerente, Torre, Squad etc.), níveis de acesso, fotos, dados contratuais e vínculos. A solução será uma aplicação em Python com Streamlit e SQLite.

🗂️ Funcionalidades principais

📋 CRUD de Pessoas
Cadastrar nova pessoa
Alterar dados
Excluir cadastro
Visualizar lista com filtros (por Squad, Grupo, Acesso etc.)

Acesso controlado: certos campos e ações só podem ser feitas por determinados níveis de permissão

🔐 Controle de Acesso Hierárquico
Níveis de acesso em ordem crescente:

Normal: Acessa as informações dentro do banco de dados que estão livres para qualquer um. Sem acessar informações sensíveis.
Operador: Acesso Normal + Poder de fazer algumas alterações no seu próprio cadastro apenas.
Coordenador: Acesso Operador + Poder de fazer alterações algumas informações em determinados membros de determinadas Squad(s).
Tower: Acesso Coordenador + Poder de fazer alterações em várias Squads determinadas de todos os membros determinados dessas squads.
Gerente: Acesso Tower + Poder de fazer qualquer alteração em qualquer squad(s) a baixo de seu comando e de qualquer membro
a seu comando na linha da gerencia incluindo informações privilegiadas.
Deus: Único e acima de todos, pode apagar qualquer um e fazer quaisquer alterações sem limitações.

🔒 Regras de permissão específicas para cada tipo, principalmente para:
Alterar acesso de outro membro
Ver e editar notas sensíveis
Deletar cadastros

📥 Campos do Cadastro de Pessoa
Foto
Nome e sobrenome
Celular
Email pessoal e corporativo
Gerência, Gestor, Torre, Coordenador
Squad
Posição (ex: PO, DEV, QA, etc.)
Contratação (Presencial/Híbrido/Home office + dias)
Tipo de contratação (PJ ou CLT)
Valor (R$)
Equipamento (Pessoal/Empresa, quais)
Descrição pessoal (livre)
Notas superiores (campo sigiloso, editável apenas por cargos superiores)
Anexo do currículo (Excluir/ Add)


🎛️ Painel lateral com filtros e busca
Pesquisar
Listagem de:

Torres
Gerências
Coordenadores
Operadores
Squads


🧪 Tecnologias e arquitetura
| Item                      | Detalhes                                          |
| ------------------------- | ------------------------------------------------- |
| **Back-end**              | Python 3                                          |
| **Banco de Dados**        | SQLite + SQLAlchemy                               |
| **Front-end**             | Streamlit                                         |
| **Criptografia de senha** | Algoritmo simples, gerando hash de 100 caracteres |
| **Execução**              | Local, servidor ou nuvem privada                  |
| **Formato**               | Modular por camadas (estilo MVC adaptado)         |


🧩 Estrutura de pastas sugerida (MVC adaptado ao Streamlit)

hapvida_ti/
│
├── app.py                      # Arquivo principal da aplicação Streamlit
├── models/                     # Modelos SQLAlchemy
│   └── pessoa.py               # Tabela Pessoa
│   └── acesso.py               # Níveis de acesso
│   └── auth.py                 # Lógica de senha e login
│
├── database/
│   └── db.py                   # Engine + criação das tabelas
│
├── controllers/               # Regras de negócio
│   └── cadastro_controller.py
│   └── login_controller.py
│
├── views/                     # Interfaces Streamlit
│   └── cadastro_view.py
│   └── login_view.py
│   └── filtro_view.py
│
├── utils/
│   └── crypto.py              # Função para criptografia simples de senha
│
├── uploads/                   # CVs e fotos
├── data/                      # banco SQLite
└── requirements.txt


📅 Plano de estudo/desenvolvimento: 20 minutos por dia
| Dia     | Tópico                     | Objetivo                                              |
| ------- | -------------------------- | ----------------------------------------------------- |
| **1**   | Planejamento               | Criar estrutura de pastas e arquivos iniciais         |
| **2**   | Modelagem                  | Criar tabela `Pessoa` e `Acesso` com SQLAlchemy       |
| **3**   | Banco de dados             | Criar `engine`, `session`, e inicializar banco        |
| **4**   | Criptografia               | Criar função de senha criptografada de 100 caracteres |
| **5**   | Cadastro básico            | Streamlit: Tela de cadastro básico de pessoa          |
| **6**   | Login e controle de acesso | Autenticação simples por email corporativo e senha    |
| **7**   | Camada de permissão        | Validar ações por nível de acesso                     |
| **8**   | Visualização filtrada      | Listar registros com filtros (Squad, Torre, etc.)     |
| **9**   | Alteração de acesso        | Tela e validação para alteração de nível              |
| **10**  | Uploads                    | Upload de foto e currículo com Streamlit              |
| **11**  | Tela de busca geral        | Painel lateral com filtros e busca                    |
| **12**  | Testes e refatoração       | Revisar e limpar código                               |
| **13+** | Extras                     | Exportar para Excel, deploy local, backups            |
