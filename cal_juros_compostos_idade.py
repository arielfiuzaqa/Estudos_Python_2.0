# Simular o investimento com aportes mensais crescentes e juros compostos

# Parâmetros
idade_final = 40
rendimento_mensal = 0.01  # 1% ao mês

# Variáveis
saldo = 0
historico = []

for idade in range(1, idade_final + 1):
    aporte_mensal = idade * 10  # Ex: 1 ano = R$10/mês, 2 anos = R$20/mês...
    for mes in range(12):
        saldo *= (1 + rendimento_mensal)  # Aplicar juros compostos
        saldo += aporte_mensal  # Adicionar aporte mensal
    historico.append((idade, aporte_mensal, round(saldo, 2)))

saldo_final = round(saldo, 2)
historico[-1], saldo_final

# Exibir o resultado final
print(f"Saldo final após {idade_final} anos: R${saldo_final}")