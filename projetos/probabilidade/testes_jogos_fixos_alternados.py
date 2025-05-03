import random
from collections import defaultdict
from tqdm import tqdm
import pandas as pd

# === Funções auxiliares ===

def gerar_jogo():
    return sorted(random.sample(range(1, 26), 15))

def contar_acertos(jogo, concurso):
    return len(set(jogo) & set(concurso))

def gerar_concursos(qtd):
    return [gerar_jogo() for _ in range(qtd)]

def simular(ciclo, num_concursos=100000000):
    concursos = gerar_concursos(num_concursos)

    jogos_fixos = [gerar_jogo() for _ in range(10)]
    resultados_fixos = defaultdict(int)
    resultados_variados = defaultdict(int)

    for _ in tqdm(range(num_concursos), desc=f"Ciclo {ciclo} - Fixos"):
        concurso = random.choice(concursos)
        for jogo in jogos_fixos:
            acertos = contar_acertos(jogo, concurso)
            if acertos >= 11:
                resultados_fixos[acertos] += 1

    for _ in tqdm(range(num_concursos), desc=f"Ciclo {ciclo} - Variados"):
        concurso = random.choice(concursos)
        for _ in range(10):
            jogo = gerar_jogo()
            acertos = contar_acertos(jogo, concurso)
            if acertos >= 11:
                resultados_variados[acertos] += 1

    faixas = [11, 12, 13, 14, 15]
    tabela = {
        "Faixa de Acertos": faixas,
        "Jogos Fixos": [resultados_fixos[i] for i in faixas],
        "Jogos Variados": [resultados_variados[i] for i in faixas]
    }
    return pd.DataFrame(tabela)

# === Execução dos 10 ciclos ===
for ciclo in range(1):
    resultado = simular(ciclo)
    print(f"\n=== RESULTADO {ciclo} ===")
    print(resultado.to_string(index=False))
