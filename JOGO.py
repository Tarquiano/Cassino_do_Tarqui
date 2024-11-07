import time
import random
import Number_Match as nb
import saldo 
import avv
import DadoSorte as ds

class cor:
    RESET = '\033[0m'    
    NEGRITO = '\033[1m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    BRANCO = '\033[97m'
    CINZA = '\033[90m'



print("Bem vindo ao cassinho do Tarqui")
time.sleep(2)
while True:
    print("Escolha uma opção:")
    print("1. Jogos")
    print("2. Saldo")
    print("3. Sair")
    
    opcao_menu = int(input("Escolha uma opção "))
    
    if opcao_menu == 1:
        while True:
            print("\nJogos:")
            time.sleep(0.50)
            print("1: Number match")
            print("2: Dado da sorte")
            print("3: Aviãonzinho")
            print("4: Sair")
            opcao_jogo = int(input("Digite o jogo (1/2/3) "))

            if opcao_jogo == 1:
                nb.number_match()
            elif opcao_jogo == 2:
                ds.dado_sorte()
                time.sleep(1)
            elif opcao_jogo == 3:
                avv.aviao()
            elif opcao_jogo == 4:
                break
            else:
                print("Opção inválida!\n")
                time.sleep(1)
    elif opcao_menu == 2:
        saldo.saldo_menu()
        time.sleep(1)
    
    elif opcao_menu == 3:
        break
    else:
        print("Opção inválida!\n")
        time.sleep(1)

print("See you later!")