#🎯 O que vamos aprender - Pandas nivel 1 - Usando planilhas reais

#📂 Abrir um arquivo Excel e selecionar a aba certa
#🧱 Ver as colunas disponíveis
#🔎 Filtrar os dados por condição (ex: STATUS = 'aprovado')
#🔄 Filtrar mais de uma condição
#🎯 Filtrar colunas específicas
#💾 Salvar os resultados filtrados

import pandas as pd

# Caminho absoluto para o arquivo Excel
caminho_arquivo = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao.xlsx"
caminho_salvar = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao_n1.xlsx"
caminho_salvar2 = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao_n2_filtrada.xlsx"

# Ver todas as abas disponíveis no arquivo Excel
excel = pd.ExcelFile(caminho_arquivo)
print(excel.sheet_names)

# 📂 Selecionando a aba da planilha
df = pd.read_excel(caminho_arquivo, sheet_name="SAC\'s")

# 🧱 Ver as colunas disponíveis, Linhas
print(f"Coluna lista = df.columns.tolist() = {df.columns.tolist()}")
print(f"Lista das {5} primeiras linhas: {df.head(5)}")

# 🔎 Filtrar os dados por condição (ex: STATUS = 'aprovado') - Repetir o processo para outras colunas
df_aprovados = df[df['STATUS'] == 'Enviado Emergencial']
print(df_aprovados)


# ====================================================================
print("# ========================================== SELECIONANDO COLUNAS ================================================")
# ✅ 1. Selecionar colunas específicas pelo nome
print("\n✅ 1. Selecionar colunas específicas pelo nome\n")
df_filtro_colunas = df[['HOMOLOGAÇÃO', 'Tipo de Objeto', 'Objeto']] 
print(df_filtro_colunas)

# ✅ 2. Selecionar colunas entre duas posições
print("\n✅ 2. Selecionar colunas entre duas posições\n")
df_fil_col_posicao = df.iloc[0:10, 8:11] # Seleciona as linhas de 0 a 10 e as colunas de 8 a 12
print(df_fil_col_posicao)

# ✅ 3. Selecionar de uma coluna até outra pelo nome (inclusive)
print("\n✅ 3. Selecionar de uma coluna até outra pelo nome (inclusive)\n")
colunas = df.columns.tolist()
inicio = colunas.index("Coordenador")
fim = colunas.index("TORRE")+1 # +1 para incluir a coluna 10
df_fil_nome = df.iloc[:, inicio: fim] # Seleciona todas as linhas e as colunas de 8 a 10
print(df_fil_nome)


# 📂 Criando um novo excell com os dados filtrados
print("\n📂 Criando um novo excell com os dados filtrados\n")

db = pd.read_excel(caminho_arquivo, sheet_name="SAC\'s")
db.columns = db.columns.str.strip().str.upper() # Substitui os espaços por underline
coluna = db.columns.tolist()
i = coluna.index("STATUS")
f = coluna.index("OBS") + 1 
# Filtrando as colunas entre STATUS e OBS
db_filtrado = db.iloc[: , i:f] # Seleciona todas as linhas e as colunas de 1 a 12
# Mostrar e salvar
print(db_filtrado.head())
db_filtrado.to_excel(caminho_salvar2, index=False) # Salva o arquivo Excel com os dados filtrados

# =============================================== PANDAS NIVEL 2 ===============================================
print("\n# ==================================== PANDAS NIVEL 2 ============================================ #\n")
#print(df.info()) # Verifica o tipo de dado de cada coluna



