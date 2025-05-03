import pandas as pd
import random
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.cell import WriteOnlyCell
from openpyxl import Workbook

# Caminhos
CAMINHO_PLANILHA_ORIGINAL = r"projetos\probabilidade\planilha jogos\loto_facil.xlsx"
CAMINHO_PLANILHA_RESULTADO = r"projetos\probabilidade\planilha jogos\jogos_gerados_e_comparados.xlsx"

# Função para carregar os concursos reais
def carregar_concursos():
    df = pd.read_excel(CAMINHO_PLANILHA_ORIGINAL, usecols="A:Q")
    concursos = []
    for _, row in df.iterrows():
        concurso = {
            'numero': row.iloc[0],
            'data': row.iloc[1],
            'numeros': sorted([int(x) for x in row.iloc[2:17]])
        }
        concursos.append(concurso)
    return concursos

# Função para gerar um jogo aleatório de 15 ou 16 números
def gerar_jogo(qtd_numeros):
    return sorted(random.sample(range(1, 26), qtd_numeros))

# Função para contar acertos
def contar_acertos(jogo, concurso):
    return len(set(jogo) & set(concurso['numeros']))

# Função principal de simulação
def simular_comparacoes(quantidade_jogos, qtd_numeros_jogo):
    concursos = carregar_concursos()
    resumo_acertos = {i: 0 for i in range(11, 16)}
    jogos_processados = 0
    print("\nIniciando processamento dos jogos...")

    wb = Workbook(write_only=True)
    ws = wb.create_sheet(title="Resultados")
    vermelho = Font(color="FF0000")

    cabecalho = ["Concurso", "Data", "Qtd Acertos"] + [f"bola {i}" for i in range(1, 16)]
    ws.append(cabecalho)

    for i in range(quantidade_jogos):
        jogo = gerar_jogo(qtd_numeros_jogo)
        melhor_acerto = 0
        melhores_concursos = []

        for concurso in concursos:
            acertos = contar_acertos(jogo, concurso)
            if acertos >= 11:
                if acertos > melhor_acerto:
                    melhor_acerto = acertos
                    melhores_concursos = [concurso]
                elif acertos == melhor_acerto:
                    melhores_concursos.append(concurso)

        if melhor_acerto >= 11:
            resumo_acertos[melhor_acerto] += 1
            for c in melhores_concursos:
                row = [c['numero'], c['data'], melhor_acerto]
                for num in c['numeros']:
                    cell = WriteOnlyCell(ws, value=num)
                    if num in jogo:
                        cell.font = vermelho
                    row.append(cell)
                ws.append(row)

        jogos_processados += 1
        if jogos_processados % 10000 == 0:
            print(f"{jogos_processados} jogos processados...")

    # Adiciona resumo ao final
    ws.append([])
    ws.append(["Resumo de Acertos"])
    ws.append(["Acertos", "Quantidade", "%"])

    for acertos in range(11, 16):
        qtd = resumo_acertos[acertos]
        percentual = (qtd / quantidade_jogos) * 100
        ws.append([acertos, qtd, f"{percentual:.2f}%"])

    wb.save(CAMINHO_PLANILHA_RESULTADO)
    print(f"\n📁 Resultados salvos em: {CAMINHO_PLANILHA_RESULTADO}")
    print("\n✅ Processamento concluído!")

# === Execução ===
if __name__ == "__main__":
    qtd_jogos = int(input("Quantos jogos deseja gerar? "))
    qtd_numeros = int(input("Quantos números por jogo (15 ou 16)? "))
    simular_comparacoes(qtd_jogos, qtd_numeros)
