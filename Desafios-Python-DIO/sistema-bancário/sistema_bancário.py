import os

opcoes = '''
    Selecione uma das opções:
    [A] Sacar
    [B] Depositar
    [C] Extrato Bancário
    [D] Sair
    '''
extrato = []
sair = False
saque = 0
LIMITE_SAQUE = 500.00
saldo = 0
mensagem = ''
limite_quantidade_saque = 3

while sair is not True:
    print(opcoes)
    opcao = input().lower()

    if opcao == 'a':

        os.system('cls')

        if limite_quantidade_saque == 0:
            print('Você atingiu o limite máximo de saques diário.')
            continue
        if saldo == 0:
            print('Saldo insuficiente')
            continue

        saque = float(input('Informe a quantidade que deseja sacar: '))
        
        if saque > LIMITE_SAQUE:
            print(f'O limite máximo de saque é de R${LIMITE_SAQUE:1.2f}.')

        elif saque > saldo:
            print('Saldo insuficiente')
        
        else:
            saldo -= saque
            mensagem = f'Saque efetuado: -R${saque:1.2f}'
            print(mensagem)
            extrato.append(mensagem)

            limite_quantidade_saque -= 1

    elif opcao == 'b':
        os.system('cls')
        deposito = float(input('Informe a quantidade para depositar: '))

        saldo += deposito

        mensagem = f'Depósito efetuado: +R${deposito:.2f}'
        print(mensagem)
        extrato.append(mensagem)
        
    elif opcao == 'c':
        os.system('cls')
        print(f'Seu saldo em conta:R${saldo:.2f}')
        print()
        for dados in extrato[::-1]:
            print(dados)
            print()
        
    elif opcao == 'd':
        os.system('cls')
        print('Você saiu do sistema! ')
        sair = True

    else:
        print('Opção desconhecida.')