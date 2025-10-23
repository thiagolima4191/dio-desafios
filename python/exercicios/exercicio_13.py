"""
Crie um programa que peça ao usuário para digitar a altitude inicial de um objeto em queda livre a partir do repouso.
Em seguida, o programa deve calcular e mostrar o tempo que o objeto leva para atingir o solo, desconsiderando a resistência do ar.
"""
import math

g = 9.81
h = float(input("Altitude inicial do objeto em metros:"))
t = math.sqrt((2*h)/g)
print(f"O objeto levará {t:.2f} segundos para atingir o solo.")