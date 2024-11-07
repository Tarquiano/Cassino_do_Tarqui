import random, time
import saldo
def aviao():
    print("\nBem vindo ao Dado da sorte!")
    print(f"""intruções:
                O computador multiplicará sua aposta a cada vez que você continuar
                Caso você não continue, você ganhará até a útima multiplicadaT
                
                A cada vez que você contina a aposta é multiplicada 0,1x
                Caso o avião bater, você perde a aposta inicial""") 
    input("Digite algo para continuar ")
    
    
    time.sleep(1)
    
    parou = False
    ganhou = False
    perdeu = False
    while True:
        aposta = float(input("Digite o valor de sua aposta: "))
        verificador = saldo.verifica_saldo(aposta)
        while verificador == False:
            aposta = float(input("\nDigite o valor da aposta "))
            verificador = saldo.verifica_saldo(aposta)
        ap_inicial = aposta
        perdeu = False

        for i, multiplicador in enumerate([1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5], start=1):
            aposta *= multiplicador
            max_random = max(80 - (i-1)*10, 10) 
            num = random.randint(1, max_random)

            if i < 10:
                numeros_perdedores = [
                    [5, 7],
                    [5, 7, 15],
                    [5, 7, 15, 25],
                    [5, 7, 15, 25, 35],
                    [5, 7, 15, 25, 35, 50],
                    [5, 7, 15, 25, 35, 50, 65],
                    [5, 7, 15, 25, 35, 50, 65, 70],
                    [5, 7, 15, 25, 35, 50, 65, 70, 80],
                    [5, 7, 15, 25, 35, 50, 65, 70, 80, 90]
                ][i-1]
            else:
                numeros_perdedores = list(range(1, 11))  # Última rodada tem mais chances de perda
                numeros_perdedores.remove(3)

            if num in numeros_perdedores:
                print("Perdeu!")
                perdeu = True
                break
            elif i == 10:
                print(f"\033[1;34mPARABÉNS VOCÊ VENCEU!! SEU SALDO É DE R${aposta:.2f}")
                ganhou = True
                break

            cntn = input("Deseja continuar? (S/N) ")
            if cntn.lower() == 'n':
                print(f"Seu saldo é de R${aposta:.2f}")
                parou = True
                break
            else:
                print("Continuando...")

        if parou == True:
            break
        if perdeu:
            break

    if parou == True:
        saldo.ganhou_aposta(aposta)

    elif perdeu == True:
        saldo.perdeu_aposta(ap_inicial)
    elif ganhou == True:
        saldo.ganhou_aposta(aposta)
    time.sleep(2)