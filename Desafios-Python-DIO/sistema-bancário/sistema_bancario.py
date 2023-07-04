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
quantidade_saque = 0
LIMITE_SAQUE = 3
saldo = 0.0
limite = 500.00

while sair is not True:
    
    print(opcoes)
    opcao = input('Informe a opção desejada: ').lower()

    if opcao == 'b':

        os.system('cls')
        valor_deposito = float(input('Informe o valor do depósito: '))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f'Depósito: +R$ {valor_deposito:.2f}')

            print(f'Depósito de R$ {valor_deposito:.2f} efetuado com sucesso!')
            
        else:
            print('Informe um valor válido')
    
    elif opcao == 'a':
        os.system('cls')
        valor_saque = float(input('Informe o valor do saque: '))

        if valor_saque > 0:
            
            excedeu_saque = valor_saque > limite

            excedeu_saldo = valor_saque > saldo

            excedeu_limite_saques = quantidade_saque >= LIMITE_SAQUE

            if excedeu_saque:
                print('Falha de Operação. Valor de saque excedido. ')
            
            elif excedeu_saldo:
                print('Falha de Operação. Saldo insuficiente. ')
            
            elif excedeu_limite_saques:
                print('Falha na Operação. Você atingiu o limite máximo de 3 saques.')
            
            else: 
                saldo -= valor_saque
                extrato.append(f'Saque: -R$ {valor_saque:.2f}')
                quantidade_saque += 1

                print(f'Saque de R$ {valor_saque:.2f} efetuado com sucesso!')
            
        else: 
            print('Operação cancelada. Valor incorreto.')

    
    elif opcao == 'c':
        os.system('cls')

        print('==========EXTRATO==========')
        print(f'Saldo Total: R$ {saldo:.2f}')
        if not extrato:
            print('Ainda não existem operações')
        
        else:
            for dados in extrato[::-1]:
                print(dados)
                print()
        print('===========================')
    
    elif opcao == 'd':
        os.system('cls')
        print(f'O Banco Python agradece a sua visita.\n')
        sair = True
    
    else:
        os.system('cls')
        print('Digite uma opção válida.')