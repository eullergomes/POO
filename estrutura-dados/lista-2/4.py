"""
Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), nome, idade, telefone.
O programa deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no 
formato chave: nome-idade-fone
"""

agenda = {}
i = 0

#cadastrar
while True:
    cpf = int(input('Digite o CPF: '))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digita a idade: '))
    telefone = int(input('Digite o telefone: '))

    agenda[i] = {'nome': nome, 'idade': idade, 'telefone': telefone}
    i += 1
    opc = input('Deseja cadastrar mais pessoas? (S/N) ')
    if opc.lower() == 'n':
        break

#imprimir
for i in agenda:
    pessoa = agenda[i]
    nome = pessoa['nome']
    idade = pessoa['idade']
    telefone = pessoa['telefone']

    print(f'\nCPF - {cpf}\nNome: {nome}, idade: {idade}, telefone: {telefone}')
    