# --- Simulador de Estratégias para Lotofácil com Comparativo de Dezenas 15 a 20 ---
# Por: Mestre Bilionário, Ser de Luz e Iluminado Celestial 👑

import os
import time
import random
import collections
import pandas as pd
import itertools
from math import comb

CAMINHO_PLANILHA = r"projetos\probabilidade\planilha jogos\loto_facil.xlsx"

# Carrega a planilha com concursos anteriores
def carregar_concursos(caminho):
    df = pd.read_excel(caminho, usecols="C:Q", skiprows=1)
    concursos = []
    for _, row in df.iterrows():
        concurso = [int(num) for num in row.values if not pd.isna(num)]
        concursos.append(concurso)
    return concursos

# Estratégias

def estrategia_equilibrada(qtd_numeros=15):
    pares = [n for n in range(2, 26, 2)]
    impares = [n for n in range(1, 26, 2)]
    max_pares = qtd_numeros // 2
    max_impares = qtd_numeros - max_pares
    jogo = random.sample(pares, max_pares) + random.sample(impares, max_impares)
    random.shuffle(jogo)
    return sorted(jogo)

def estrategia_fechamento_simples(qtd_numeros=15):
    universo = list(range(1, 26))
    escolhidos = random.sample(universo, 20)
    jogo = random.sample(escolhidos, qtd_numeros)
    return sorted(jogo)

def estrategia_sem_padroes_ruins(qtd_numeros=15):
    while True:
        universo = list(range(1, 26))
        jogo = sorted(random.sample(universo, qtd_numeros))
        sequencia = 1
        for i in range(1, len(jogo)):
            if jogo[i] == jogo[i-1] + 1:
                sequencia += 1
                if sequencia >= 5:
                    break
            else:
                sequencia = 1
        else:
            pares = sum(1 for n in jogo if n % 2 == 0)
            impares = qtd_numeros - pares
            if 5 <= pares <= 10 and 5 <= impares <= 10:
                return jogo

def contar_combinacoes_vencedoras(jogo_gerado, concurso):
    contagem = collections.Counter()
    for combinacao in itertools.combinations(jogo_gerado, 15):
        acertos = len(set(combinacao) & set(concurso))
        if acertos >= 11:
            contagem[acertos] += 1
    return contagem, comb(len(jogo_gerado), 15)

def simular_estrategias_por_dezena(concursos, estrategias, qtd_numeros, max_jogos=100000):
    print(f"\nSimulando estratégias para {qtd_numeros} dezenas...")
    resultados = {nome: {15:0, 14:0, 13:0, 12:0, 11:0, 'total': 0, 'combinacoes': 0} for nome in estrategias.keys()}

    for nome, funcao in estrategias.items():
        for i in range(max_jogos):
            idx = random.randint(0, len(concursos)-1)
            concurso = concursos[idx]
            jogo = funcao(qtd_numeros)

            acertos_dict, num_combs = contar_combinacoes_vencedoras(jogo, concurso)
            for pontos, quantidade in acertos_dict.items():
                resultados[nome][pontos] += quantidade

            resultados[nome]['total'] += 1
            resultados[nome]['combinacoes'] += num_combs

            if (i+1) % (max_jogos // 10) == 0:
                print(f"{nome} ({qtd_numeros} dezenas): {i+1} jogos concluídos", end='\r')

    return max_jogos, resultados

def exibir_relatorio_completo(resultados_por_dezena):
    premios = {15: 1_000_000, 14: 2000, 13: 48, 12: 12, 11: 6}
    valor_base = {
        15: 3.00, 16: 48.00, 17: 408.00, 18: 2448.00,
        19: 11628.00, 20: 46512.00
    }

    for dezenas, resultados in resultados_por_dezena.items():
        print("\n" + "="*117)
        print(f"\n=== RELATÓRIO COMPLETO PARA {dezenas} DEZENAS ===")
        print(f"Jogos gerados: {next(iter(resultados.values()))['total']}")
        print(f"Combinações de 15 dezenas avaliadas: {next(iter(resultados.values()))['combinacoes']}")

        print("\n=== RELATÓRIO FINAL DE DESEMPENHO ===\n")
        print(f"{'Estratégia':<30}{'15 acertos':<12}{'14 acertos':<12}{'13 acertos':<12}{'12 acertos':<12}{'11 acertos':<12}")
        print("-" * 90)
        for estrat, dados in resultados.items():
            print(f"{estrat:<30}{dados[15]:<12}{dados[14]:<12}{dados[13]:<12}{dados[12]:<12}{dados[11]:<12}")

        print("\n=== RELATÓRIO DE PORCENTAGEM DE ACERTOS ===\n")
        print(f"{'Estratégia':<30}{'15 acertos (%)':<18}{'14 acertos (%)':<18}{'13 acertos (%)':<18}{'12 acertos (%)':<18}{'11 acertos (%)':<18}")
        print("-" * 110)
        for estrat, dados in resultados.items():
            total_comb = dados['combinacoes'] or 1
            print(f"{estrat:<30}{(dados[15]/total_comb)*100:<18.2f}{(dados[14]/total_comb)*100:<18.2f}{(dados[13]/total_comb)*100:<18.2f}{(dados[12]/total_comb)*100:<18.2f}{(dados[11]/total_comb)*100:<18.2f}")

        print("\n=== RELATÓRIO FINANCEIRO ===\n")
        print(f"{'Estratégia':<30}{'Investido (R$)':<18}{'Ganho (R$)':<18}{'Lucro (R$)':<18}{'ROI (%)':<10}")
        print("-" * 80)
        for estrat, dados in resultados.items():
            total_jogos = dados['total']
            investido = total_jogos * valor_base[dezenas]
            ganho = sum(dados.get(p, 0) * premios[p] for p in premios)
            lucro = ganho - investido
            roi = (lucro / investido * 100) if investido > 0 else 0
            print(f"{estrat:<30}R$ {investido:<16.2f}R$ {ganho:<16.2f}R$ {lucro:<16.2f}{roi:.2f}%")

# Execução principal
if __name__ == "__main__":
    concursos = carregar_concursos(CAMINHO_PLANILHA)

    input_dezenas = input("\nInforme as quantidades de dezenas (ex: 15,16,17 ou 15-20): ").strip()
    dezenas_escolhidas = []

    if '-' in input_dezenas:
        ini, fim = map(int, input_dezenas.split('-'))
        dezenas_escolhidas = list(range(ini, fim+1))
    else:
        dezenas_escolhidas = [int(x) for x in input_dezenas.split(',')]

    max_jogos = int(input("Quantos jogos deseja gerar por faixa de dezenas? "))

    estrategias = {
        "Combinação Equilibrada": estrategia_equilibrada,
        "Fechamento Simples": estrategia_fechamento_simples,
        "Sem Padrões Ruins": estrategia_sem_padroes_ruins
    }

    resultados_por_dezena = {}

    for d in dezenas_escolhidas:
        _, resultados = simular_estrategias_por_dezena(concursos, estrategias, d, max_jogos)
        resultados_por_dezena[d] = resultados

    exibir_relatorio_completo(resultados_por_dezena)
