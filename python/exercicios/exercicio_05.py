"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1=float(input("Digite um numero:"))
num2=float(input("Digite um numero:"))
num3=float(input("Digite um numero:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} foi o maior numero digitado.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} foi o maior numero digitado.")
else:
    print(f"{num3} foi o maior numero digitado.")
    
if num1 < num2 and num1 < num3:
    print(f"{num1} foi o menor numero digitado.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} foi o menor numero digitado.")
else:
    print(f"{num3} foi o menor numero digitado.")