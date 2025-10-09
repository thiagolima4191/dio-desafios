import random
import os
import time # Para adicionar um pequeno delay e melhorar a experiência

def limpar_tela():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def valida_int(pergunta, min_val, max_val):
    """
    Valida se a entrada do usuário é um inteiro dentro de um range específico.
    Inclui tratamento de erro para entrada não numérica.
    """
    while True:
        try:
            x = int(input(pergunta))
            if min_val <= x <= max_val:
                return x
            else:
                print(f"Opção inválida! Digite um número entre {min_val} e {max_val}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

def obter_nome_jogada(numero_jogada):
    """Retorna o nome da jogada com base no número."""
    if numero_jogada == 1:
        return "Pedra"
    elif numero_jogada == 2:
        return "Papel"
    elif numero_jogada == 3:
        return "Tesoura"
    return "Inválida"

def determinar_vencedor_rodada(jogador1_jogada, jogador2_jogada):
    """
    Determina o vencedor de uma única rodada.
    Retorna 1 se Jogador 1 vencer, 2 se Jogador 2 vencer, 0 para empate.
    """
    if jogador1_jogada == jogador2_jogada:
        return 0  # Empate
    elif (jogador1_jogada == 1 and jogador2_jogada == 3) or \
         (jogador1_jogada == 2 and jogador2_jogada == 1) or \
         (jogador1_jogada == 3 and jogador2_jogada == 2):
        return 1  # Jogador 1 vence
    else:
        return 2  # Jogador 2 (computador) vence

def exibir_placar(vitorias_j1, vitorias_j2, empates):
    """Exibe o placar atual do jogo."""
    print("\n--- PLACAR GERAL ---")
    print(f"Vitórias do Jogador 1: {vitorias_j1}")
    print(f"Vitórias do Computador: {vitorias_j2}")
    print(f"Empates: {empates}")
    print("--------------------")

# --- Variáveis de Contagem (inicializadas no escopo principal) ---
vitorias_jogador1 = 0
vitorias_computador = 0
total_empates = 0
historico_jogadas = [] # Para armazenar o histórico de cada rodada

# --- Loop Principal do Jogo ---
def jogar_jokenpo():
    global vitorias_jogador1, vitorias_computador, total_empates, historico_jogadas

    limpar_tela()
    print("=========================")
    print("      JOGUE JOKENPÔ!     ")
    print("=========================")

    while True:
        print("\nEscolha sua jogada:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        print("0 - Sair do Jogo")
        print("-------------------------")

        jogada_jogador1 = valida_int("Digite o número da sua escolha: ", 0, 3)

        if jogada_jogador1 == 0:
            print("\nSaindo do jogo. Até a próxima!")
            break # Sai do loop principal

        jogada_computador = random.randint(1, 3)

        historico_jogadas.append((jogada_jogador1, jogada_computador))

        print(f"\nVocê escolheu: {obter_nome_jogada(jogada_jogador1)}")
        print(f"O Computador escolheu: {obter_nome_jogada(jogada_computador)}")
        time.sleep(1.5) # Pequena pausa para suspense!

        resultado_rodada = determinar_vencedor_rodada(jogada_jogador1, jogada_computador)

        if resultado_rodada == 1:
            print(">>> VOCÊ VENCEU ESTA RODADA! <<<")
            vitorias_jogador1 += 1
        elif resultado_rodada == 2:
            print(">>> O COMPUTADOR VENCEU ESTA RODADA! <<<")
            vitorias_computador += 1
        else:
            print(">>> EMPATE NESTA RODADA! <<<")
            total_empates += 1
        
        exibir_placar(vitorias_jogador1, vitorias_computador, total_empates)
        time.sleep(2) # Pausa para o jogador ver o placar

# --- Executa o jogo ---
if __name__ == "__main__":
    jogar_jokenpo()

    # --- Exibição Final do Histórico e Resultados ---
    limpar_tela()
    print("=========== RESUMO DO JOGO ===========")
    print("Histórico de Jogadas:")
    if not historico_jogadas:
        print("Nenhuma rodada jogada.")
    else:
        for i, (j1, j2) in enumerate(historico_jogadas):
            print(f"Rodada {i+1}: Você ({obter_nome_jogada(j1)}) vs Computador ({obter_nome_jogada(j2)})")

    exibir_placar(vitorias_jogador1, vitorias_computador, total_empates)

    if vitorias_jogador1 > vitorias_computador:
        print("\nVOCÊ É O GRANDE VENCEDOR DO JOGO!")
    elif vitorias_computador > vitorias_jogador1:
        print("\nO COMPUTADOR VENCEU O JOGO!")
    else:
        print("\nO JOGO TERMINOU EM EMPATE GERAL!")
    print("======================================")