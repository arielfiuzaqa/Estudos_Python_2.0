valor_a = 25000
valor_b = 0
meses = 0
rendimento = 1.01  # 1% ao mês

while valor_b <= valor_a:
    valor_a = valor_a * rendimento + 600
    valor_b = valor_b * rendimento + 2500
    meses += 1


print(f"Você ultrapassará a outra pessoa em {meses} meses.")
print(f"Seu saldo: R${valor_b:,.2f} | Saldo da outra pessoa: R${valor_a:,.2f}")

while valor_b < 2 * valor_a:
    valor_a = valor_a * rendimento + 600
    valor_b = valor_b * rendimento + 2500
    meses += 1

print(f"Você terá o dobro do valor da outra pessoa em {meses} meses.")
print(f"Seu saldo: R${valor_b:,.2f} | Saldo da outra pessoa: R${valor_a:,.2f}")

