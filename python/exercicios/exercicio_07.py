"""
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7\*altura)
"""

nome=(input("Infomer seu nome:"))
idade=(int(input("Informe sua idade:")))
altura=(float(input("Informe sua altura:")))
peso=(float(input("Informe seu peso:")))

imc = peso / (altura ** 2)

print(f"Olá {nome} seu IMC é {imc:.2f}.")