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
saldo = 0.0
limite_quantidade_saque = 3

# Função Sacar
def sacar(valor_saque, saldo_total):
    if valor_saque > LIMITE_SAQUE:
        print(f'Limite máximo de saque: R${LIMITE_SAQUE}')

        return False
    
    elif valor_saque <= saldo_total and valor_saque >= 0:
        saldo_total -= valor_saque

        return saldo_total
    
    else:
       print('Saldo Insuficiente.')

# Função Depositar
def depositar(valor_deposito, saldo_total):
   if valor_deposito > 0:
        saldo_total += valor_deposito
        print(f'Depósito efetuado com Sucesso.')

        return saldo_total
   
   else:
       print('Valor inválido')

       return saldo_total


while sair is not True:

    print(opcoes)
    escolhe_opcao = input().lower()
    os.system('cls')

# Opção de saque:    
    if escolhe_opcao == 'a':
        if limite_quantidade_saque > 0: 
            try:
                saque = float(input('Informe o valor para sacar: '))

            except ValueError:
                print('Valor Incorreto.')

            else: 
                if sacar(saque, saldo):
                    saldo = sacar(saque, saldo)
                    extrato.append(f'Saque Efetuado -R${saque:.2f}.')
                    limite_quantidade_saque -=1
                    print('Saque efetuado com sucesso!')
        else:
            print('Você atingiu o limite de saques diários.')

# Opção de demósito
    elif escolhe_opcao == 'b':        
        try:
            deposito = float(input('Informe o valor do depósito: '))
            
        except ValueError:
            print('Valor Incorreto.')

        else:
            saldo = depositar(deposito, saldo)
            extrato.append(f'Depósito Efetuado +{deposito}.')

# Opção de extrato
    elif escolhe_opcao == 'c':
        print('Seu saldo: R$',saldo)
        for dados in extrato[::-1]:
            print(dados)

#opcao de sair
    elif escolhe_opcao == 'd':
        sair = True
        print('Você saiu do sistema')
    
    else:
        print('Opção desconhecida')

