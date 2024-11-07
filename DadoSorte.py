import time, random, saldo


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



def dado_sorte():
            perdeu = 0
            print("\nBem vindo ao Dado da sorte!")
            time.sleep(1)
            print(f"""intruções:
                Você escolherá um número de 2 a 12 e dois dados serão jogados.
                serão jogados 2 dados de seis lados
                Caso a soma dos dados resulte no número no qual você escolheu, você ganha
                {cor.NEGRITO}Você terá 2 chances de jogar os dados{cor.RESET}
                
                Primeira tentativa (Aposta 5,0x)
                Segunda tentativa (Aposta 2,5x)
                Caso a soma dos dados não bater com o seu número, o valor apostado será perdido""") 
            input("Digite algo para continuar ")
            
            valor_aposta = float(input("Digite o valor da aposta: "))
            verificador = saldo.verifica_saldo(valor_aposta)
            while verificador == False:
                valor_aposta = float(input("Digite o valor da aposta: "))
                verificador = saldo.verifica_saldo(valor_aposta)
            
            
            while True:
                number_user = int(input("Digite o seu número (de 2 a 12): "))
                if (number_user > 12) or (number_user < 2):
                    print("Por favor, digite um número válido")
                    time.sleep(2)
                else:
                    break
            for i in range(0, 2):
                input("aperte Enter para jogar o primeiro dado ")
                time.sleep(0.5)
                dado1 = random.randint(1, 6)
                print("O primeiro dado foi jogado")
                time.sleep(1)
                input("aperte Enter para jogar o segundo dado ")
                time.sleep(0.5)
                dado2 = random.randint(1, 6)
                print("O segundo dado foi jogado")
                print("O resultado dos dados foi...")
                time.sleep(1)
                print(f"Primeiro dado: {dado1}")
                time.sleep(0.5)
                print(f"Segundo dado: {dado2}")
                time.sleep(1)
                
                print(f"\nSoma dos dados: {dado1 + dado2}")
                time.sleep(1.3)
                if (dado1 + dado2 == number_user):
                    print(f"Parabéns, você {cor.VERDE}ganhou{cor.RESET} a aposta")
                    if perdeu == 1:
                        valor_aposta = valor_aposta * 2.5
                    else:
                        valor_aposta = valor_aposta * 5
                    saldo.ganhou_aposta(valor_aposta)
                    break
                
                elif perdeu == 1:
                    print(f"Infelizmente não foi dessa vez, você {cor.VERMELHO}perdeu{cor.RESET} a aposta")
                    saldo.perdeu_aposta(valor_aposta)
                
                else:
                    print(f"Infelizmente não foi dessa vez, você tem mais {cor.AMARELO}UMA{cor.RESET} chance")
                    perdeu += 1