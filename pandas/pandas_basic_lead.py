import pandas as pd

# Caminho absoluto para o arquivo Excel
caminho_arquivo = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao.xlsx"
caminho_arquivo2 = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao2.xlsx"

# Ler o arquivo Excel
df = pd.read_excel(caminho_arquivo, sheet_name="SAC's")

# FASE 1 – INICIANTE: Lendo arquivos Excel e CSV
# Vendo as abas do arquivo Excel
xls = pd.ExcelFile(caminho_arquivo)
print(f"Sheet Names: {xls.sheet_names}")

# Imprimir o DataFrame diferentess atributos
"""print(f"df: {df}")
print(f"df.head():\n{df.head()}")
print(f"df.columns: {df.columns}")
print(f"df.dtypes: {df.dtypes}")
print(f"df.shape: {df.shape}")"""

# Fase 2 – INTERMEDIÁRIO: Manipulando dados
# ✅ Renomeando colunas
df.rename(columns={'SAC': 'SACTI', 'STATUS': 'status'}, inplace=True)
print(f"df['SAC']:\n{df['SACTI']}")
# ✅ Renomeando linhas
df.rename(index={0: 'SAC', 1: 'Soim', 2: 'Madalena', 3: 'Jesus'}, inplace=True)
print(f"df.index:\n{df.index}")
# Filtrando alguns pontos planilha
df_filtrado1 = df['SACTI'] # Varios valores inclusive os repetidos da coluna 'SAC'
df_filtrado2 = df['SACTI'].unique() # Apenas os valores unicos da coluna 'SAC'
df_lista_filtrado = df['SACTI'].tolist() # Lista com os valores unicos da coluna 'SAC'
print(f"df_filtrado1: {df_filtrado1} \n df_filtrado2: {df_filtrado2} \n df_lista_filtrado: {df_lista_filtrado}")
#print(f'STATUS: {df["STATUS"].value_counts()}')
print(f"colunas: {df.columns}")



# FASE 4 – PROFISSIONAL: Trabalhando com arquivos grandes e dados bagunçados
# ✅ Substituir texto ou valores
df['status'] = df['status'].replace('Publicação Semanal', 'Diária')
print(f"df['STATUS']:\n{df['status']}")
# Salvando alterações fase 4
fase4_save = df.to_excel(caminho_arquivo2, sheet_name="SAC\'s", index=False)
print(f"fase4_save: {fase4_save}")

# Filtrando informações da planilha
df_filtrado3 = df.loc[df['status'] == 'Diária']



