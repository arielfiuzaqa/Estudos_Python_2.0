# Modo básico para o abrir documentos do google sheets - baixando o documento toda vez. Ainda falta melhorar muito
import pandas as pd

# Aberturas dos arquivos, pode ser .xlsx ou .csv ou direto da planilha do google sheets
arquivo_basic = r"C:\\Users\\t_ariel.fiuza\Downloads\\python triton\\pandas\\docs\\Planilhao_n2_filtrada.xlsx"
arquivo_intermediario = "https://hapvida.sharepoint.com/:x:/s/QualidadeeTestes/EdUnemMvTgtEn7AUsun0n2EBkG460BFhiLnIOwt-2Etb3g?e=crRrbE&nav=MTVfezkyODAzMUNELUNFMDAtNDQ5NC04RjcwLThBRTJBODJBOEIzQn0"

#df = pd.read_excel(arquivo_basic, sheet_name="Sheet1") # Lê a aba 1 do arquivo Excel - aquivo_basic
# df = pd.read_csv(arquivo_basic, sheet_name="aba2") # Lê a aba 2 do arquivo csv
df = pd.read_excel(arquivo_intermediario, sheet_name="SAC\'s") # Lê a aba 1 do arquivo Excel - aquivo_intermediario

print(df.head()) # Mostra as 5 primeiras linhas do dataframe
#df.info() # Mostra as informações do dataframe
#df.describe() # Mostra as estatísticas do dataframe
#df.columns # Mostra os nomes das colunas do dataframe
