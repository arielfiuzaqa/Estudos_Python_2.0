# Script para compilar planilhas de publicação em um único arquivo chamado 'Planilhao.xlsx'
# Autor: Devilson Mestre Python
# Requisitos: pandas, openpyxl

import os
import pandas as pd
from datetime import datetime

# Pasta onde estão as planilhas de entrada
PASTA_PLANILHAS = r"C:\Users\t_ariel.fiuza\Downloads\PLANILHAO"

# Dicionário para armazenar dados compilados
compilado = {}

# Função para converter versão em float com base no número após o ponto (ex: 1.782 -> 782)
def versao_float(v):
    try:
        v = str(v).strip()
        if not v or v.lower() == 'nan':
            return None
        partes = v.split(".")
        return int(partes[1]) if len(partes) > 1 else 0
    except:
        return None

# Função para limpar strings para comparação
def limpar(s):
    return str(s).strip().replace(" ", "").lower()

# Função para processar uma aba de uma planilha
def processar_aba(df, data_referencia):
    for _, row in df.iterrows():
        tipo = str(row[3]).strip()
        nome = str(row[4]).strip()
        versao = str(row[5]).strip()
        caminho = str(row[6]).strip()
        analista = str(row[7]).strip()
        torre = str(row[10]).strip()

        if not nome or not caminho or not versao:
            continue  # ignora linhas sem dados importantes

        versao_convertida = versao_float(versao)
        if versao_convertida is None:
            continue  # ignora se versão inválida

        chave = (limpar(nome), limpar(caminho))

        if chave not in compilado:
            compilado[chave] = {
                "Tipo de Objeto": tipo,
                "Objeto": nome,
                "Versão": versao,
                "Versão Interna": versao_convertida,
                "Caminho CVS": caminho,
                "Analista": analista,
                "Torre": torre,
                "Data Modificação": data_referencia
            }
        else:
            atual = compilado[chave]
            if versao_convertida > atual["Versão Interna"]:
                atual["Versão"] = versao
                atual["Versão Interna"] = versao_convertida
                atual["Data Modificação"] = data_referencia
            if limpar(analista) != limpar(atual["Analista"]):
                atual["Analista"] = analista
                atual["Data Modificação"] = data_referencia

# Função para detectar data no nome do arquivo
def extrair_data(nome_arquivo):
    try:
        partes = nome_arquivo.split("-")
        dia = int(partes[-3])
        mes = int(partes[-2])
        ano = int(partes[-1].split(".")[0])
        return f"{dia:02d}/{mes:02d}/{ano}"
    except:
        return "Data Não Identificada"

# Processa todas as planilhas na pasta
for nome_arquivo in os.listdir(PASTA_PLANILHAS):
    if nome_arquivo.endswith(".xlsx"):
        caminho_arquivo = os.path.join(PASTA_PLANILHAS, nome_arquivo)
        data_ref = extrair_data(nome_arquivo)

        try:
            xl = pd.ExcelFile(caminho_arquivo)
            if nome_arquivo.startswith("TAB PLANILHA DE PUBLICAÇÃO SEMANAL"):
                for aba in ["SAC's Semanal", "PARA DAR BAIXA"]:
                    if aba in xl.sheet_names:
                        df = xl.parse(aba)
                        processar_aba(df, data_ref)
            elif nome_arquivo.startswith("PLANILHA DE PUBLICAÇÃO DIÁRIA"):
                if "SAC's Diária" in xl.sheet_names:
                    df = xl.parse("SAC's Diária")
                    processar_aba(df, data_ref)
        except Exception as e:
            print(f"Erro ao processar {nome_arquivo}: {e}")

# Converte para DataFrame final e salva
linhas = []
for (nome, caminho), dados in compilado.items():
    linhas.append([
        dados["Tipo de Objeto"],
        dados["Objeto"],
        dados["Versão"],
        dados["Caminho CVS"],
        dados["Analista"],
        dados["Torre"],
        dados["Data Modificação"]
    ])

df_final = pd.DataFrame(linhas, columns=[
    "Tipo de Objeto", "Objeto", "Versão", "Caminho CVS", "Analista", "TORRE", "Data Modificação"
])

# Salvar como Planilhao.xlsx na mesma pasta do script
df_final.to_excel("Planilhao.xlsx", index=False)
print("✅ Planilha 'Planilhao.xlsx' criada com sucesso!")
