def calcular_viabilidade_produto_automatizado_v3():
    """
    Calcula a viabilidade de um produto para marketing de afiliados,
    utilizando estimativas de mercado para CPC e CVR em cada plataforma.
    Inclui análise para iniciar com baixos valores.
    """

    print("--- Calculadora Inteligente de Viabilidade de Produto para Afiliados ---")
    print("Vamos descobrir se seu produto tem potencial de lucro em cada plataforma de anúncios.")
    print("Você só precisa me dizer sobre seu produto e o lucro que espera!")
    print("-" * 75)

    # --- Dados de Entrada do Usuário ---
    try:
        valor_produto = float(input("1. Qual o PREÇO DE VENDA do produto na Shopee (R$)? Ex: 100.00: "))
        percentual_comissao = float(input("2. Qual o PERCENTUAL da sua comissão (ex: 9 para 9%)? ")) / 100
        roi_desejado_percentual = float(input("3. Qual o RETORNO SOBRE INVESTIMENTO (ROI) MÍNIMO que você quer? (Ex: 150 para 150%) ")) / 100
    except ValueError:
        print("\nERRO: Por favor, insira apenas números válidos. Tente novamente.")
        return

    # --- Cálculos Básicos (Não precisam de input do usuário) ---
    comissao_por_venda = valor_produto * percentual_comissao
    print(f"\nSua COMISSÃO BRUTA por Venda (CBV): R$ {comissao_por_venda:,.2f}")

    if comissao_por_venda <= 0:
        print("ERRO: A comissão por venda deve ser maior que zero. Verifique os dados.")
        return

    # CPA de Ponto de Equilíbrio (ROI de 100% - o máximo que pode gastar para não perder dinheiro)
    cpa_ponto_equilibrio = comissao_por_venda / 1.00
    print(f"Custo por Aquisição (CPA) de PONTO DE EQUILÍBRIO (ROI 100%): R$ {cpa_ponto_equilibrio:,.2f}")
    print(f"  (Você pode gastar até R$ {cpa_ponto_equilibrio:,.2f} por venda para não ter prejuízo.)")

    # CPA Máximo para atingir o ROI desejado (o máximo que pode gastar para ter o lucro que você quer)
    cpa_maximo_desejado = comissao_por_venda / roi_desejado_percentual
    print(f"CPA MÁXIMO para atingir seu ROI de {roi_desejado_percentual * 100:.0f}%: R$ {cpa_maximo_desejado:,.2f}")
    print(f"  (Você precisa gastar MENOS de R$ {cpa_maximo_desejado:,.2f} por venda para ter o lucro desejado.)")

    # --- Análise por Plataforma (AUTOMATIZADA com Médias de Mercado) ---
    print("\n--- Analisando a Viabilidade em Cada Plataforma (Baseado em Médias do Mercado) ---")
    print("Estas são ESTIMATIVAS. Seus resultados podem variar muito com a qualidade do seu vídeo!")
    print("-" * 75)

    # Dicionário de plataformas com CPC e CVR médios (ajustados para o Brasil e afiliados/vídeo)
    # Importante: CVR para Shopee considera o efeito do cookie (qualquer compra).
    plataformas = {
        "Google Ads (Rede de Pesquisa)": {
            "cpc_medio": 3.50, # Custo por clique em anúncios de texto na busca
            "cvr_media": 0.02 # 2% de conversão: 2 a cada 100 cliques compram
        },
        "Instagram Ads (Meta Ads - Reels/Stories)": {
            "cpc_medio": 0.70, # Custo por clique em anúncios de vídeo
            "cvr_media": 0.009 # 0.9% de conversão: 9 a cada 1000 cliques compram
        },
        "TikTok Ads": {
            "cpc_medio": 0.50, # Custo por clique em anúncios de vídeo
            "cvr_media": 0.007 # 0.7% de conversão: 7 a cada 1000 cliques compram
        }
    }

    # Variável para rastrear se alguma plataforma mostrou potencial
    alguma_plataforma_promissora = False

    for plataforma, dados in plataformas.items():
        cpc_medio = dados["cpc_medio"]
        cvr_media = dados["cvr_media"]

        # CPA Estimado na Plataforma
        cpa_estimado_plataforma = cpc_medio / cvr_media
        lucro_por_venda_estimado = comissao_por_venda - cpa_estimado_plataforma
        roi_estimado_plataforma = (comissao_por_venda / cpa_estimado_plataforma) * 100 if cpa_estimado_plataforma > 0 else float('inf')

        print(f"\n### {plataforma} ###")
        print(f"  > **Estimativas Usadas:** CPC Médio: R$ {cpc_medio:,.2f} | CVR Média: {cvr_media * 100:.1f}%")
        print(f"  > Seu CPA ESTIMADO nesta plataforma: R$ {cpa_estimado_plataforma:,.2f}")
        print(f"  > Seu ROI ESTIMADO nesta plataforma: {roi_estimado_plataforma:,.0f}%")
        print(f"  > Lucro/Prejuízo LÍQUIDO por Venda Estimado: R$ {lucro_por_venda_estimado:,.2f}")

        if lucro_por_venda_estimado >= 0 and cpa_estimado_plataforma <= cpa_maximo_desejado:
            print(f"  **VEREDITO: POTENCIALMENTE LUCRATIVO! ✅**")
            print(f"  Com as médias do mercado, este produto parece ter uma BOA CHANCE de atingir ou superar seu ROI desejado de {roi_desejado_percentual * 100:.0f}%.")
            alguma_plataforma_promissora = True
        elif lucro_por_venda_estimado >= 0 and cpa_estimado_plataforma > cpa_maximo_desejado:
            print(f"  **VEREDITO: POUCO LUCRATIVO (ou abaixo do esperado). ⚠️**")
            print(f"  Com as médias do mercado, você provavelmente teria lucro, mas abaixo do seu ROI desejado de {roi_desejado_percentual * 100:.0f}%.")
            print("  **PLANO DE AÇÃO:** Você precisaria de vídeos e segmentação MUITO melhores para reduzir o custo ou aumentar a conversão. Veja as dicas abaixo!")
            alguma_plataforma_promissora = True # Ainda há potencial para otimização
        else:
            print(f"  **VEREDITO: PROVÁVEL PREJUÍZO! ❌**")
            print(f"  Com as médias do mercado, este produto provavelmente te faria perder dinheiro por venda.")
            print("  **PLANO DE AÇÃO:** NÃO ANUNCIE ASSIM! Repense este produto/plataforma. Talvez uma comissão maior ou um produto com mais apelo (que gere mais cliques/vendas) sejam necessários. Ou um vídeo GENIAL!")
    
    print("\n--- Estratégia para Iniciar e Ter Sucesso (Mesmo com Dúvidas Iniciais) ---")
    print("Mesmo que as projeções não sejam perfeitas, começar com pouco é crucial para o aprendizado:")
    
    if not alguma_plataforma_promissora:
        print("\n**ATENÇÃO:** Nenhuma plataforma pareceu altamente promissora com as médias atuais para este produto.")
        print("Isso indica que este produto (com essa comissão e seu ROI desejado) é um DESAFIO considerável.")
        print("Considere **fortemente** encontrar um produto com **MAIOR COMISSÃO** ou **MAIOR APELO VIRAL**.")
        print("Se ainda assim quiser testar este produto, comece com um orçamento MÍNIMO e foque em vídeos EXCEPCIONAIS.")

    print("\n1. **Comece PEQUENO (Orçamento de Teste):**")
    print(f"   Use seus primeiros R$ 50 - R$ 100 (do seu total de R$ 400) para testes em UMA plataforma por vez (ex: TikTok).")
    print("   O objetivo é coletar dados REAIS de CPC e CVR para o SEU vídeo e produto.")
    print("2. **Crie VÁRIOS VÍDEOS Diferentes (e bons!):**")
    print("   Não faça só um. Teste 2-3 ganchos, músicas, CTAs e estilos para o mesmo produto.")
    print("   Um vídeo pode ter performance 10x melhor que outro, mudando sua viabilidade por completo!")
    print("3. **Foque nos Clicks e no Cookie da Shopee:**")
    print("   Seu objetivo primário é levar a pessoa para o site da Shopee. Mesmo que ela não compre o produto do vídeo, o cookie pode render comissões de outras compras.")
    print("4. **Monitore e Otimize DIARIAMENTE:**")
    print("   Se uma campanha não estiver dando cliques ou estiver muito cara (CPA real > CBV), PAUSE-A! Não tenha medo de cortar o que não funciona.")
    print("   Se uma campanha estiver boa, AUMENTE O ORÇAMENTO GRADUALMENTE.")
    print("5. **O Aprendizado é o MAIOR Retorno Inicial:**")
    print("   Mesmo se os primeiros testes não derem lucro, cada real gasto é um real investido no seu conhecimento prático em marketing de afiliados. Este conhecimento é o que te fará ganhar muito dinheiro no futuro.")
    
    print("\n--- Fim da Análise Detalhada ---")
    print("Sua persistência e capacidade de otimização farão a diferença!")

# Chama a função para rodar o script
calcular_viabilidade_produto_automatizado_v3()