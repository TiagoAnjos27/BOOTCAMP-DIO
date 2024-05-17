# DEFINIR O TEMPO DE EXECUÇÃO DE UM COMANDO PARA OUTRO
from time import sleep

# TELA INICIAL COM MENU DE OPÇÕES
sistema = 'SISTEMA BANCÁRIO'
print('\033[32m{:=^40}\033[m'.format(sistema))
print('\033[32m[1]\033[m - Sacar')
print('\033[32m[2]\033[m - Depositar')
print('\033[32m[3]\033[m - Extrato')
print('\033[32m[4]\033[m - Sair')
print('\033[32m=\033[m'*40)

# DEFINIÇÃO DE VARIÁVEIS
saldo = 1000
limite = 500
saques = []
depositos = []
numero_saques = 0
LIMITE_SAQUE = 3

# VALIDAÇÃO SIMPLES DO MENU DE OPÇÕES
while True:
    option = str(input('\033[32mDigite uma opção:\033[m '))
    if option not in "1234" or option == "":
        print('\033[31mOpção inválida!\033[m')
        print('\033[32m-\033[m' * 40)
# LÓGICA DAS OPÇÕES
    if option == "1":
        print('Você escolheu a opção \033[4;32mSAQUE\033[m')
        print('\033[32m-\033[m'*40)
        valor_saque = float(input("Digite a quantia a sacar: "))
        while True:
            if valor_saque < 0:
                print("\033[31mValores negativos não permitidos\033[m")
                break

            if valor_saque > saldo:
                print("\033[31mSaldo Insuficiente!\033[m")
                print('\033[32m-\033[m' * 40)
                break
            if valor_saque > limite:
                print("\033[31mOperção não realizada!\033[m"
                      "\nVocê deve sacar até R$ 500,00")
                print('\033[32m-\033[m' * 40)
                break
            if numero_saques == LIMITE_SAQUE:
                print("\033[31mLimite de saque atingido!\033[m\nTente novamente em 24h.\n"
                      "Obrigado e volte sempre!")
                print('\033[32m-\033[m' * 40)
                break
            if valor_saque < saldo and numero_saques <= LIMITE_SAQUE:
                saques.append(valor_saque)
                numero_saques += 1
                saldo -= valor_saque
                print(f"\033[32mOperção realizada com sucesso!\033[m"
                      f"\nVocê sacou \033[4;32mR$ {valor_saque:.2f}\033[m ")
                print('\033[32m-\033[m'*40)
                #print(saldo)
                break

    if option == "2":
        while True:
            print('Você escolheu a opção \033[32mDEPOSITAR\033[m')
            print('\033[32m-\033[m'*40)
            deposito = float(input("Digite o valor a ser depositado: "))
            if deposito < 0:
                print("\033[31mValores negativos não permitidos\033[m")
                break
            depositos.append(deposito)
            print(f"\033[32mOperação realizada com\033[m \033[4;32mSUCESSO!\033[m\n"
                  f"Voçê depositou \033[4;33mR$ {deposito:.2f}\033[m")
            print('\033[32m-\033[m'*40)
            saldo += deposito
            break

    if option == "3":
        print("\033[32m{:=^40}\033[m".format('EXTRATO BANCÁRIO'))
        # MENU SAQUE
        if len(saques) != 0:
            print("\033[32m{:-^40}\033[m".format('SEUS SAQUES'))
        if len(saques) == 1:
            print(f"\033[33m1º Saque:\033[m R$ {saques[0]}")
            print('\033[32m=\033[m'*40)
        if len(saques) == 2:
            print(f"\033[33m1º Saque:\033[m R$ {saques[0]}\n"
                  f"\033[33m2º Saque:\033[m R$ {saques[1]}")
            print(f"\033[33mTotal:\033[m R$ {sum(saques)}")
            print('\033[32m=\033[m'*40)
        if len(saques) == 3:
            print(f"\033[33m1º Saque:\033[m R$ {saques[0]}\n"
                  f"\033[33m2º Saque:\033[m R$ {saques[1]}\n"
                  f"\033[33m3º Saque:\033[m R$ {saques[2]}")
            print(f"\033[33mTotal:\033[m R$ {sum(saques)}")
            print('\033[32m=\033[m'*40)
        # MENU DEPÓSITO
        if len(depositos) != 0:
            print("\033[32m{:-^40}\033[m".format('SEUS DEPOSITOS'))
        if len(depositos) == 1:
            print(f"\033[33m1ºDepósito:\033[m R$ {depositos[0]}")
            print('\033[32m=\033[m'*40)
        if len(depositos) == 2:
            print(f"\033[33m1ºDepósito:\033[m R$ {depositos[0]}\n"
                  f"\033[33m2ºDepósito:\033[m R$ {depositos[1]}")
            print(f"\033[33mTotal:\033[m R$ {sum(depositos)}")
            print('\033[32m=\033[m'*40)
        if len(depositos) == 3:
            print(f"\033[33m1ºDepósito:\033[m R$ {depositos[0]}\n"
                  f"\033[33m2ºDepósito:\033[m R$ {depositos[1]}\n"
                  f"\033[33m3ºDepósito:\033[m R$ {depositos[2]}")
            print(f"\033[33mTotal:\033[m R$ {sum(depositos)}")
            print('\033[33m=\033[m'*40)
        print(f"\033[33mSaldo Atual:\033[m R$ {saldo:.2f}")
        print('\033[32m=\033[m'*40)

    if option == "4":
        print('\033[31m-\033[m' * 40)
        print('\033[31mSaindo do sistema...\033[m')
        print('\033[31m-\033[m' * 40)
        sleep(1.5)
        break



