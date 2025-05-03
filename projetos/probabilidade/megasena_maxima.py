# --- Simulador de Estratégias para Mega-Sena ---
# Por: Mestre Bilionário, Ser de Luz e Iluminado Celestial 👑

# === Importações necessárias ===
import pandas as pd
import random
import os
import collections
import time

# === Configurações Iniciais ===
CAMINHO_PLANILHA = r"projetos\probabilidade\planilha jogos\mega_sena.xlsx"

# === Etapa 1: Carregar a Planilha e Concursos ===
def carregar_concursos(caminho):
    df = pd.read_excel(caminho, usecols="C:H", skiprows=1)
    concursos = []
    for _, row in df.iterrows():
        concurso = [int(num) for num in row.values if not pd.isna(num)]
        concursos.append(concurso)
    return concursos

# === Etapa 2: Estratégias de geração de jogos ===

# Estratégia 1: Frequência Alta
def estrategia_frequencia(concursos_passados):
    contador = collections.Counter()
    for concurso in concursos_passados:
        contador.update(concurso)
    mais_frequentes = [num for num, _ in contador.most_common(6)]
    return sorted(mais_frequentes)

# Estratégia 2: Atraso Alto
def estrategia_atraso(concursos_passados):
    ultimo_concurso = {}
    for idx, concurso in enumerate(concursos_passados):
        for num in concurso:
            ultimo_concurso[num] = idx
    atrasados = sorted(ultimo_concurso.items(), key=lambda x: x[1])
    mais_atrasados = [num for num, _ in atrasados[:6]]
    return sorted(mais_atrasados)

# Estratégia 3: Combinação Equilibrada
def estrategia_equilibrada(_=None):
    pares = [n for n in range(2, 61, 2)]
    impares = [n for n in range(1, 61, 2)]
    jogo = random.sample(pares, 3) + random.sample(impares, 3)
    random.shuffle(jogo)
    return sorted(jogo[:6])

# Estratégia 4: Fechamento Simples
def estrategia_fechamento_simples(_=None):
    universo = list(range(1, 61))
    escolhidos = random.sample(universo, 12)
    jogo = random.sample(escolhidos, 6)
    return sorted(jogo)

# Estratégia 5: Eliminação de Padrões Ruins
def estrategia_sem_padroes_ruins(_=None):
    while True:
        universo = list(range(1, 61))
        jogo = sorted(random.sample(universo, 6))

        # Verificar sequência longa
        sequencia = 1
        for i in range(1, len(jogo)):
            if jogo[i] == jogo[i-1] + 1:
                sequencia += 1
                if sequencia >= 4:
                    break
            else:
                sequencia = 1
        else:
            # Verificar equilíbrio par/ímpar
            pares = sum(1 for n in jogo if n % 2 == 0)
            impares = 6 - pares
            if 2 <= pares <= 4 and 2 <= impares <= 4:
                return jogo

# === Etapa 3: Comparar Jogos com Concursos ===
def comparar_jogo_concurso(jogo_gerado, concurso_real):
    acertos = len(set(jogo_gerado) & set(concurso_real))
    return acertos

# === Nova Etapa: Simular todas as estratégias até atingir 6 acertos ===
def simular_todas_estrategias(concursos, estrategias):
    resultados = {nome: {6:0, 5:0, 4:0, 'total': 0} for nome in estrategias.keys()}
    total_jogos = 0
    atingiu_meta = False

    while not atingiu_meta:
        idx = random.randint(0, len(concursos)-1)
        concurso = concursos[idx]

        for nome, funcao in estrategias.items():
            if nome in ["Combinação Equilibrada", "Fechamento Simples", "Sem Padrões Ruins"]:
                jogo = funcao()
            else:
                jogo = funcao(concursos[:idx])

            acertos = comparar_jogo_concurso(jogo, concurso)
            if acertos in resultados[nome]:
                resultados[nome][acertos] += 1
            resultados[nome]['total'] += 1

            if acertos == 6:
                print(f"\nMeta atingida pela estratégia: {nome}")
                atingiu_meta = True
                break

        total_jogos += 1

        if total_jogos % 500 == 0:
            print(f"Jogos realizados: {total_jogos}", end='\r')

    return total_jogos, resultados

# === Função para gerar relatório final ===
def gerar_relatorio_final(resultados):
    print("\n=== RELATÓRIO FINAL DE DESEMPENHO ===\n")
    print(f"{'Estratégia':<30}{'6 acertos':<12}{'5 acertos':<12}{'4 acertos':<12}")
    print("-" * 70)

    for estrategia, dados in resultados.items():
        linha = f"{estrategia:<30}"
        for pontos in [6, 5, 4]:
            linha += f"{dados.get(pontos, 0):<12}"
        print(linha)

# === Função para gerar relatório percentual ===
def gerar_relatorio_percentual(resultados):
    print("\n=== RELATÓRIO DE PORCENTAGEM DE ACERTOS ===\n")
    print(f"{'Estratégia':<30}{'6 acertos (%)':<16}{'5 acertos (%)':<16}{'4 acertos (%)':<16}")
    print("-" * 70)

    for estrategia, dados in resultados.items():
        total = dados.get('total', 1)
        linha = f"{estrategia:<30}"
        for pontos in [6, 5, 4]:
            percentual = (dados.get(pontos, 0) / total) * 100 if total > 0 else 0
            linha += f"{percentual:.2f}%{'':<11}"
        print(linha)

# === Execução Principal ===
if __name__ == "__main__":
    concursos = carregar_concursos(CAMINHO_PLANILHA)

    estrategias = {
        "Frequência Alta": estrategia_frequencia,
        "Atraso Alto": estrategia_atraso,
        "Combinação Equilibrada": estrategia_equilibrada,
        "Fechamento Simples": estrategia_fechamento_simples,
        "Sem Padrões Ruins": estrategia_sem_padroes_ruins
    }

    print("\nIniciando simulação...")
    total_jogos, resultados_finais = simular_todas_estrategias(concursos, estrategias)

    print("\n=== Resultado Final ===")
    print(f"Total de jogos realizados: {total_jogos}\n")
    gerar_relatorio_final(resultados_finais)
    gerar_relatorio_percentual(resultados_finais)
