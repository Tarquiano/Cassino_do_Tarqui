import time

saldo = 250.00
def conferir_saldo():
    time.sleep(1)
    print(f"\nSeu saldo é de {saldo:.2f}\n")
    time.sleep(2)

def perdeu_aposta(aposta):
    global saldo
    saldo -= aposta

def ganhou_aposta(aposta):
    global saldo
    saldo += aposta

def atualizar_saldo(senha, valor):
    global saldo
    if senha == 1234:
        saldo += valor
        print("Operação concluída")
    else:
        print("Senha inválida")

def verifica_saldo(aposta):
    if aposta > saldo:
        print("Aposta maior que o saldo disponível! Operação não permitida.")
        return False
    return True

def saldo_menu():
    while True:
        print("\nMenu do saldo:")
        print("1. Verificar saldo")
        print("2. Depositar")
        print("3. Sair")
        saldo_opcao = int(input("Sua opção: "))
        
        if saldo_opcao == 1:
            conferir_saldo()
        
        elif saldo_opcao == 2:
            password = int(input("\nDigite a senha númerica de 4 dígitos: "))
            novo_valor = float(input("Digite o valor do depósito: "))
            atualizar_saldo(password, novo_valor)
            time.sleep(2)
        
        elif saldo_opcao == 3:
            break
