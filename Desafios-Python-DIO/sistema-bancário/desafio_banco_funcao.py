'''
Criar 5 funções

função saque -> * saldo, valor, extrato, limite, numero_saques
    retorno saldo e extrato

função depósito -> / saldo, valor, extrato
    retorno saldo e extrato

função extrato -> saldo / * extrato

Criar função Usuário:
 função usuário para cadastro -> nome, data de nascimento, cpf 
 endereço{logradouro, numero, bairro, cidade, sigla estado}
Não deve haver o cadastro de dois usuários com o mesmo cpf

Função Conta Corrente -> agencia, número da conta, usuário.
deve ser armazenado em uma lista. 
toda conta tem o número da agência 0001, mas os número da conta 
começa do 1 e vai sequencialmente.

'''

import os


def menu():
    print('==============MENU==============')
    opcoes = '''
    Selecione uma das opções:

    [S] \tSacar
    [D] \tDepositar
    [E] \tExtrato 
    [NC] \tNova Conta
    [NU] \tNovo Usuário
    [L] \tListar Contas
    [SA] \tSair
    '''
    print(opcoes)
    op = input('Digite uma opção: ').lower()
    return op

def saque(*,saldo, limite, limite_saque, numero_saques, dados_extrato):
    valor = float(input('Informe o valor do saque: '))

    if valor > 0:
            
        excedeu_saque = valor > limite

        excedeu_saldo = valor > saldo

        excedeu_limite_saques = numero_saques >= limite_saque

        if excedeu_saque:
            print('Operação Cancelada: Valor de saque excedido. ')  
        
        elif excedeu_saldo:
            print('Saldo Insuficiente para o Saque. ')   
        
        elif excedeu_limite_saques:
            print('Falha na Operação. Você atingiu o limite máximo de 3 saques.')
        
        else: 
            saldo -= valor
            dados_extrato = f'Saque: -R$ {valor:.2f}'
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} efetuado com sucesso!')

            
    else: 
        print('Operação falhou! Valor incorreto.')
    
    return saldo, dados_extrato, numero_saques  
        
def deposito(saldo, extrato, /):
    valor = float(input('Informe o valor do depósito: '))

    if valor > 0:
        saldo += valor
        extrato = f'Depósito +RS {valor:.2f}'
        print(f'Depósito de R$ {valor:.2f} efetuado com sucesso.')

        return saldo, extrato
    
    else:
        print('Valor Inválido')

        return saldo, extrato

def extrato(saldo, /,*,args):
    print('==========EXTRATO==========')
    print(f'Saldo Total: \tR$ {saldo:.2f}')
    print()
    for valores in args[::-1]:
        print(f'\t{valores}')
    print('===========================')

def cadastro_usuario(lista_usuario):
    verifica_cpf = []

    usuario = dict.fromkeys(['nome', 'data_nascimento', 'cpf', 'endereco'])
    endereco_usuario = dict.fromkeys(['logradouro', 'numero', 'bairro', 'cidade', 'sigla'])
    usuario.update(endereco=endereco_usuario)

    for dados in usuario:
        if dados == 'endereco':
            for local in usuario['endereco']:
                print(f'{local}: ', end='')
                informacao = input()
                usuario['endereco'][local] = informacao
        
        else:
            print(f'{dados}: ', end='')
            informacao = input()

            if dados == 'cpf':
                for indice in lista_usuario:
                    verifica_cpf.append(indice['cpf'])

                while True:
                    if informacao in verifica_cpf:
                        print('CPF já cadastrado!')
                        informacao = input('Digite um novo CPF: ')
                    else:
                        break
            usuario[dados] = informacao

    os.system('cls')
    
    print(f'Usuário ',usuario['nome'], 'cadastrado')
    return usuario
   
def cadastro_conta(*,lista_usuario, conta):
    os.system('cls')
    AGENCIA = '0001'
    dicionario_contas= dict.fromkeys(['conta', 'agencia', 'usuario'])
    verifica_usuario=[]
    usuario = input('Informe o nome do Usuário: ')

    for nome in lista_usuario:
        verifica_usuario.append(nome['nome'])

    if usuario in verifica_usuario:
        dicionario_contas['conta'] = str(conta)
        dicionario_contas['agencia'] = AGENCIA
        dicionario_contas['usuario'] = usuario

        os.system('cls')
        print(f'O usuário {usuario} foi cadastrado.')
        print('Conta: ', str(conta), 'Agência: ', AGENCIA)
    
        return dicionario_contas
    
    else: 
        os.system('cls')
        print('Usuário não cadastrado.')

def listar_contas(contas):
    print(f'=============== Lista de Contas ===============\n')
    
    for dado in contas:
        conta = dado['conta']
        agencia = dado['agencia']
        usuario = dado['usuario']

        print(f'Usuário: {usuario} | Conta: {conta} | Agencia: {agencia}')


def main():
    LIMITE_SAQUE = 3
    limite = 500.00

    conta = 1
    conta_corrente = []
    lista_usuarios = []
    lista_extrato = []
    dados_extrato = ''
    numero_saques = 0
    saldo = 0.0

    while True:

        opcao = menu()
        os.system('cls')
        if opcao == 'd':

            saldo, dados_extrato = deposito(saldo, dados_extrato)
            lista_extrato.append(dados_extrato)
            
        elif opcao == 's':

            saldo, dados_extrato, numero_saques = saque(saldo=saldo, 
                                                    limite=limite, 
                                                    dados_extrato=dados_extrato, 
                                                    limite_saque=LIMITE_SAQUE, 
                                                    numero_saques=numero_saques
                                                    )
            lista_extrato.append(dados_extrato)
        
        elif opcao == 'e':

            extrato(saldo, args=lista_extrato)
        
        elif opcao == 'nc':
            if lista_usuarios:
               verifica_conta = cadastro_conta(lista_usuario=lista_usuarios, conta=conta)
               if verifica_conta:
                   conta_corrente.append(verifica_conta)
                   conta +=1

            else:
                os.system('cls')
                print('É necessário primeiro cadastrar pelo menos 1 usuário.')
        
        elif opcao == 'nu':

            lista_usuarios.append(cadastro_usuario(lista_usuarios))
          
        
        elif opcao == 'l':
            if conta_corrente:
                listar_contas(conta_corrente)
            else:
                print('Não existe(m) conta(s) cadastrada(s).')
        
        elif opcao == 'sa':
            print('============== Até Logo ==============\n')
            print('O Banco Python agradece a sua visita.')
            print()
            break

main()
