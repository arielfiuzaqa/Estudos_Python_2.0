# --- Capturador de Resultados da Quina usando Selenium ---
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# === Configurações iniciais ===
PASTA_SALVAMENTO = r"projetos/probabilidade/planilha jogos"
ARQUIVO_SAIDA = os.path.join(PASTA_SALVAMENTO, "quina.xlsx")

# Garante que a pasta existe
if not os.path.exists(PASTA_SALVAMENTO):
    os.makedirs(PASTA_SALVAMENTO)

# Inicializa o navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessa o site da Quina
driver.get("https://loterias.caixa.gov.br/Paginas/Quina.aspx")
time.sleep(5)  # Aguarda o site carregar

resultados = []

# Capturar concursos individualmente usando a área de busca de resultados
for concurso_num in range(1, 6717):  # Concurso 1 até 6716
    try:
        print(f"Capturando concurso {concurso_num}...")
        
        # Clica no botão "Resultados Anteriores"
        #.get(f"https://loterias.caixa.gov.br/Paginas/Quina.aspx")
        time.sleep(0.5)

        # Preenche o número do concurso
        campo_concurso = driver.find_element(By.ID, "buscaConcurso")
        campo_concurso.clear()
        campo_concurso.send_keys(str(concurso_num))
        campo_concurso.send_keys(Keys.ENTER)
        
        #botao_buscar = driver.find_element(By.ID, "btnBuscar")
        #botao_buscar.click()
        
        time.sleep(0.5)  # Tempo para o resultado carregar

        # Pega os dados
        data_sorteio = driver.find_element(By.XPATH, "//span[@class='ng-binding']").text
        dezenas = driver.find_elements(By.XPATH, "//ul[@class='numbers quina']//li")

        bolas = []
        for dezena in dezenas:
            bolas.append(int(dezena.text.strip()))
        
        if len(bolas) == 5:
            resultados.append({
                "Concurso": concurso_num,
                "Data": data_sorteio,
                "Bola 1": bolas[0],
                "Bola 2": bolas[1],
                "Bola 3": bolas[2],
                "Bola 4": bolas[3],
                "Bola 5": bolas[4],
            })
        
    except Exception as erro:
        print(f"⚠️ Erro ao capturar concurso {concurso_num}: {erro}")

# Fecha o navegador
driver.quit()

# Cria o DataFrame
df = pd.DataFrame(resultados)

# Organiza ordem decrescente
df = df.sort_values(by="Concurso", ascending=False)

# Salva em Excel
df.to_excel(ARQUIVO_SAIDA, index=False)

print(f"\n✅ Resultados salvos em: {ARQUIVO_SAIDA}")
