
"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra=input("Digite uma letra: ").upper()

if(
    letra == "A"
    or letra == "E"
    or letra == "I"
    or letra == "O"
    or letra == "U"
    
):
    print("Vogal")
else:
    print("Consoante")