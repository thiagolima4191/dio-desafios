"""
Crie um programa que peça ao usuário para digitar o valor inicial de um investimento,
a taxa de juros mensal e o número de meses que o valor ficou investido. Em seguida, o programa deve calcular e mostrar 
o valor final do investimento, considerando o uso de juros compostos.
"""

valor_inicial = float(input("Valor inicial do investimento (R$):"))
taxa_juros = float(input("Taxa de juros mensal(%):"))
meses = int(input("Número de meses:"))

taxa_juros/=100
valor_final = valor_inicial*(1 + taxa_juros)**meses

print(f"Valor final do investimento: R$ {valor_final:.2f}")