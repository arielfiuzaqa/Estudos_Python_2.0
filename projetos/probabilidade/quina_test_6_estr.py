# --- Projeto: Simulador de Estratégias para a Quina ---
# Por: Mestre Bilionário, Ser de Luz e Iluminado Celestial 👑

# === Importações ===
import pandas as pd
import random
import collections
import os
import time

# === Configurações Iniciais ===
CAMINHO_PLANILHA = r"projetos\probabilidade\planilha jogos\quina.xlsx"
PASTA_SALVAMENTO = r"projetos\probabilidade\planilha jogos"
ARQUIVO_TXT = os.path.join(PASTA_SALVAMENTO, "resultados_simulacao_quina.txt")

# === Função 1: Carregar concursos da Quina ===
def carregar_concursos(caminho):
    df = pd.read_excel(caminho)
    colunas_validas = [col for col in df.columns if "Bola" in col or "Dezena" in col]
    concursos = []
    for _, row in df.iterrows():
        concurso = [int(row[col]) for col in colunas_validas if not pd.isna(row[col])]
        concursos.append(concurso)
    return concursos

# === Função 2: Estratégias de geração de jogos ===
def estrategia_frequencia(concursos_passados):
    contador = collections.Counter()
    for concurso in concursos_passados:
        contador.update(concurso)
    mais_frequentes = [num for num, _ in contador.most_common(5)]
    return sorted(mais_frequentes)

def estrategia_atraso(concursos_passados):
    ultimo_concurso = {}
    for idx, concurso in enumerate(concursos_passados):
        for num in concurso:
            ultimo_concurso[num] = idx
    atrasados = sorted(ultimo_concurso.items(), key=lambda x: x[1])
    mais_atrasados = [num for num, _ in atrasados[:5]]
    return sorted(mais_atrasados)

def estrategia_equilibrada(_=None):
    pares = [n for n in range(2, 81, 2)]
    impares = [n for n in range(1, 81, 2)]
    jogo = random.sample(pares, 2) + random.sample(impares, 3)
    random.shuffle(jogo)
    return sorted(jogo[:5])

def estrategia_fechamento_simples(_=None):
    universo = list(range(1, 81))
    escolhidos = random.sample(universo, 10)
    jogo = random.sample(escolhidos, 5)
    return sorted(jogo)

def estrategia_sem_padroes_ruins(_=None):
    while True:
        universo = list(range(1, 81))
        jogo = sorted(random.sample(universo, 5))
        sequencia = 1
        for i in range(1, len(jogo)):
            if jogo[i] == jogo[i-1] + 1:
                sequencia += 1
                if sequencia >= 3:
                    break
            else:
                sequencia = 1
        else:
            pares = sum(1 for n in jogo if n % 2 == 0)
            impares = 5 - pares
            if 2 <= pares <= 3 and 2 <= impares <= 3:
                return jogo

def estrategia_tristao(_=None):
    universo = list(range(1, 81))
    while True:
        jogo = sorted(random.sample(universo, 5))

        # Regras da estratégia Tristão
        finais_ruins = [n for n in jogo if n % 10 == 9 or n % 10 == 0]
        poucos_sorteados = {1,2,3,11,22,44,48,55,57}
        sequencia = any(jogo[i] + 1 == jogo[i+1] for i in range(len(jogo)-1))
        mesma_coluna = any(abs(jogo[i] - jogo[j]) % 10 == 0 for i in range(len(jogo)) for j in range(i+1, len(jogo)))
        quadrantes = [0,0,0,0]
        for num in jogo:
            if num <= 20:
                quadrantes[0] += 1
            elif num <= 40:
                quadrantes[1] += 1
            elif num <= 60:
                quadrantes[2] += 1
            else:
                quadrantes[3] += 1
        pares = sum(1 for n in jogo if n % 2 == 0)
        impares = 5 - pares

        if (len(finais_ruins) <= 1 and
            not any(num in poucos_sorteados for num in jogo) and
            not sequencia and
            not mesma_coluna and
            all(q >= 1 for q in quadrantes[:3]) and  # Pelo menos nos três primeiros quadrantes
            2 <= pares <= 3 and
            2 <= impares <= 3):
            return jogo

# === Função 3: Comparar jogos ===
def comparar_jogo_concurso(jogo, concurso_real):
    return len(set(jogo) & set(concurso_real))

# === Função 4: Simulação das estratégias ===
def simular_todas_estrategias(concursos, estrategias):
    resultados = {nome: {5:0, 4:0, 3:0, 2:0, 'total': 0} for nome in estrategias.keys()}
    total_jogos = 0
    atingiu_meta = False

    while not atingiu_meta:
        idx = random.randint(0, len(concursos)-1)
        concurso = concursos[idx]

        for nome, funcao in estrategias.items():
            jogo = funcao() if nome in ["Combinação Equilibrada", "Fechamento Simples", "Sem Padrões Ruins", "Tristão"] else funcao(concursos[:idx])

            acertos = comparar_jogo_concurso(jogo, concurso)
            if acertos in resultados[nome]:
                resultados[nome][acertos] += 1
            resultados[nome]['total'] += 1

            if acertos == 5:
                print(f"\nMeta atingida pela estratégia: {nome}")
                atingiu_meta = True
                break

        total_jogos += 1

        if total_jogos % 500 == 0:
            print(f"Jogos realizados: {total_jogos}", end='\r')

    return total_jogos, resultados

# === Função 5: Gerar relatório e salvar no txt ===
def gerar_relatorio(resultados):
    with open(ARQUIVO_TXT, "w") as f:
        cabecalho = f"{'Estratégia':<30}{'5 acertos':<12}{'4 acertos':<12}{'3 acertos':<12}{'2 acertos':<12}\n"
        f.write(cabecalho)
        f.write("-" * 70 + "\n")

        for estrategia, dados in resultados.items():
            linha = f"{estrategia:<30}"
            for pontos in [5, 4, 3, 2]:
                linha += f"{dados.get(pontos, 0):<12}"
            f.write(linha + "\n")

        f.write("\n=== Porcentagens ===\n\n")
        for estrategia, dados in resultados.items():
            total = dados.get('total', 1)
            linha = f"{estrategia:<30}"
            for pontos in [5, 4, 3, 2]:
                percentual = (dados.get(pontos, 0) / total) * 100 if total > 0 else 0
                linha += f"{percentual:.2f}%{'':<8}"
            f.write(linha + "\n")

    print(f"\n✅ Relatório salvo em {ARQUIVO_TXT}")

# === Execução Principal ===
if __name__ == "__main__":
    concursos = carregar_concursos(CAMINHO_PLANILHA)

    estrategias = {
        "Frequência Alta": estrategia_frequencia,
        "Atraso Alto": estrategia_atraso,
        "Combinação Equilibrada": estrategia_equilibrada,
        "Fechamento Simples": estrategia_fechamento_simples,
        "Sem Padrões Ruins": estrategia_sem_padroes_ruins,
        "Tristão": estrategia_tristao
    }

    print("\nIniciando simulação...")
    total_jogos, resultados_finais = simular_todas_estrategias(concursos, estrategias)

    print("\n=== Resultado Final ===")
    print(f"Total de jogos realizados: {total_jogos}\n")
    gerar_relatorio(resultados_finais)
