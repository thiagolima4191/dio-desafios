print("LANCHONETE")
print("1 - Coxinha R$5,00")
print("2 - Pastel R$7,00")
print("3 - Café R$4,00")
print("4 - Suco R$6,00")
print("5 - Sair")

total = 0
while True:
    op = int(input("Qual item gostaria de comprar? "))
    qtd = int(input("Quantas unidades quer comprar? "))
    
    if (op == 1):
        total = total + qtd * 5.00

    elif (op == 2):
        total = total + qtd * 7.00
        
    elif(op == 3):
        total = total + qtd * 4.00
    
    elif(op == 4):
        total = total + qtd * 6.00
        
    elif(op == 5):
        break
    
    else:
        print("Produto invalido. Selecione outro. ")
        
print(f"O total a ser gasto neste pedido é de R$ {total}.")