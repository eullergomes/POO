"""
Considere um sistema onde os dados são armazenados em dicionários. Nesse sistema existe um dicionario principal e o 
dicionário de backup. Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu 
conteúdo. Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e excluindo os dados do 
dicionário principal quando ele atingir tamanho 5
"""

dict_principal = {}
dict_backup = {}
tam = 0

while True:
    #cadastro dos dados
    print('\nINSERIR DADOS:')
    nome = str(input('Digite o nome: '))
    cpf = int(input('Digite o CPF: '))
    idade = int(input('Digite a idade: '))

    dict_principal[cpf] = {'nome': nome, 'idade': idade}
    dict_backup[cpf] = {'nome': nome, 'idade': idade}

    tam += 1 #tamanho do dicionário

    opc = str(input('Deseja cadastrar mais dados? (S/N) '))
    if opc.lower() == 'n':
        print('\nDados inseridos:')
        print(dict_backup)
        break

    if (tam == 5):
        print('\nTamanho máximo atingido!')
        print('Dicionário principal RESETADO:')

        dict_principal.clear()
        tam = 0

        opc = str(input('\nDeseja imprimir todos os dados já inseridos? (S/N) '))

        if opc.lower() == 's':
            print(dict_backup)