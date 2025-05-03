# --- Projeto: Gerador e Automatizador de Jogos da Lotofácil ---
# Por: Mestre Bilionário, Ser de Luz e Iluminado Celestial 👑

import pandas as pd
import random
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# === Configurações Iniciais ===
CAMINHO_PLANILHA = r"projetos\probabilidade\planilha jogos\loto_facil.xlsx"
PASTA_SALVAMENTO = r"projetos\probabilidade\planilha jogos"
ARQUIVO_TXT = os.path.join(PASTA_SALVAMENTO, "jogos_gerados_lotofacil.txt")

def preparar_pasta_arquivo():
    if not os.path.exists(PASTA_SALVAMENTO):
        os.makedirs(PASTA_SALVAMENTO)
    with open(ARQUIVO_TXT, "w") as f:
        f.write("")

# === Estratégia: Combinação Equilibrada ===
def estrategia_equilibrada(qtd_numeros):
    pares = [n for n in range(2, 26, 2)]
    impares = [n for n in range(1, 26, 2)]
    max_pares = qtd_numeros // 2
    max_impares = qtd_numeros - max_pares
    jogo = random.sample(pares, max_pares) + random.sample(impares, max_impares)
    random.shuffle(jogo)
    return sorted(jogo)

# === Estratégia: Fechamento Simples ===
def estrategia_fechamento_simples(qtd_numeros):
    universo = list(range(1, 26))
    escolhidos = random.sample(universo, 20)
    jogo = random.sample(escolhidos, qtd_numeros)
    return sorted(jogo)

def gerar_jogos(quantidade_jogos, qtd_numeros):
    jogos_gerados = []
    metade = quantidade_jogos // 2

    for _ in range(metade):
        jogos_gerados.append(tuple(estrategia_equilibrada(qtd_numeros)))
    for _ in range(metade):
        jogos_gerados.append(tuple(estrategia_fechamento_simples(qtd_numeros)))

    if quantidade_jogos % 2 != 0:
        estrategia_extra = random.choice([
            lambda: estrategia_equilibrada(qtd_numeros),
            lambda: estrategia_fechamento_simples(qtd_numeros)
        ])
        jogos_gerados.append(tuple(estrategia_extra()))

    return jogos_gerados

def salvar_jogos(jogos):
    with open(ARQUIVO_TXT, "w") as f:
        for idx, jogo in enumerate(jogos, 1):
            linha = f"Jogo {idx}: {' '.join(str(num).zfill(2) for num in jogo)}\n"
            f.write(linha)
    print(f"\n{len(jogos)} jogos gerados e salvos em {ARQUIVO_TXT} ✅")

def preencher_jogos_web(jogos):
    print("\nIniciando automação do navegador... 🚀")
    service = Service(ChromeDriverManager().install())
    bot = webdriver.Chrome(service=service)

    try:
        bot.get("https://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/")
        time.sleep(5)
        bot.find_element(By.LINK_TEXT, "Aposte agora").click()
        time.sleep(5)
        input("\n💬 Faça login na conta Caixa e pressione ENTER para continuar...")

        for idx, jogo in enumerate(jogos, 1):
            print(f"Preenchendo jogo {idx}...")
            novo_jogo_btn = bot.find_element(By.XPATH, "//button[contains(text(),'Lotofácil')]")
            novo_jogo_btn.click()
            time.sleep(2)

            for numero in jogo:
                numero_formatado = str(numero).zfill(2)
                xpath_numero = f"//button[contains(text(),'{numero_formatado}')]"
                try:
                    numero_botao = bot.find_element(By.XPATH, xpath_numero)
                    ActionChains(bot).move_to_element(numero_botao).click().perform()
                    time.sleep(0.2)
                except Exception as e:
                    print(f"⚠️ Número {numero_formatado} não encontrado: {e}")

            confirma_btn = bot.find_element(By.XPATH, "//button[contains(text(),'Incluir')]")
            confirma_btn.click()
            time.sleep(2)

        print("\n✅ Todos os jogos preenchidos! Agora finalize o pagamento manualmente.")

    except Exception as erro:
        print(f"⚠️ Ocorreu um erro durante a automação: {erro}")

if __name__ == "__main__":
    preparar_pasta_arquivo()
    quantidade = int(input("\nQuantos jogos novos deseja gerar? "))
    while True:
        qtd_numeros = int(input("Quantos números por jogo? (15 ou 16): "))
        if qtd_numeros in [15, 16]:
            break
        print("❌ Entrada inválida. Digite 15 ou 16.")
    
    jogos = gerar_jogos(quantidade, qtd_numeros)

    print("\n=== Jogos Gerados ===")
    for idx, jogo in enumerate(jogos, 1):
        print(f"Jogo {idx}: {' '.join(str(num).zfill(2) for num in jogo)}")

    salvar_jogos(jogos)

    escolha = input("\nDeseja preencher os jogos automaticamente no site? (s/n): ").strip().lower()
    if escolha == 's':
        preencher_jogos_web(jogos)
    else:
        print("\n✅ Encerrado apenas com a criação e salvamento dos jogos!")
