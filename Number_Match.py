import time, random
import saldo
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

def number_match():
            print("\nBem vindo ao Number Match!")
            time.sleep(1)
            print("""intruções:
                Você terá que escolher um número aleatório dependendo
                da dificuldade.
                
                1: Fácil: de 1 a 5  (Aposta 1,5x)
                2: Médio: de 1 a 10 (Aposta 2,0x)
                3: dificil:de 1 a 50 (Aposta 5,0x)
                Caso você não acerte o número, perderá o valor apostado""") 
            input("Digite algo para continuar ")
            
            op_jogo1 = int(input("Selecione a dificuldade (1/2/3) "))
            ap = float(input("Digite o valor da aposta "))
            verificador = saldo.verifica_saldo(ap)
            while verificador == False:
                ap = float(input("Digite o valor da aposta: "))
                verificador = saldo.verifica_saldo(ap)
            
            if op_jogo1 == 1:            ## SISTEMA DA APOSTA
                numero_jogo1 = random.randint(1, 5)

            elif op_jogo1 == 2:
                numero_jogo1 = random.randint(1, 10)
            
            elif op_jogo1 == 3:
                numero_jogo1 = random.randint(1, 50)
            
            
            print(numero_jogo1) # TESTE
            escolha_jogo1 = int(input("Digite o número: "))
           
            
            print(f"{cor.NEGRITO}O número está...{cor.RESET}")
            time.sleep(1)
            
            if escolha_jogo1 == numero_jogo1:  ## RESULTADOS E MUDANÇA NO SALDO
                print(f"{cor.VERDE}CORRETO{cor.RESET}")
                print("Você ganhou a aposta!")
                time.sleep(2)
                if op_jogo1 == 1:
                    ap = ap * 1  # Multiplicador para o primeiro nível
                elif op_jogo1 == 2:
                    ap = ap * 2  # Multiplicador para o segundo nível
                elif op_jogo1 == 3:
                    ap = ap * 5  # Multiplicador para o terceiro nível

                
                saldo.ganhou_aposta(ap)
            else:
                print(f"{cor.VERMELHO}ERRADO{cor.RESET}")  # Perdeu
                print("Você perdeu a aposta!")
                time.sleep(2)
                saldo.perdeu_aposta(ap)