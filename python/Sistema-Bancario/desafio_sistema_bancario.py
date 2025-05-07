
# Aqui são criadas as variáveis principais do sistema.
def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
=============== MENU ================
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
=====================================
    => """

# Cria um laço infinito onde o menu é mostrado sempre até o usuário digitar q (sair). A variável opcao guarda o que o usuário escolheu.
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Encerrando o sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida. Tente novamente.")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Aqui são feitas várias verificações antes de permitir o saque
def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

# Mostra todas as movimentações gravadas na lista extrato e o saldo atual.
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
main()
