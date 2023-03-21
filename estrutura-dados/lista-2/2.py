#Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e depois coloque em um dicionário. Depois remova todas as pessoas menores de 18 anos do dicionário e coloque em outro dicionário

pessoas = {}

#cadastro
while True:
    cpf = int(input('Digite o CPF: '))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))

    pessoas[cpf] = {'nome': nome, 'idade': idade}

    opc = str(input('Gostaria de cadastrar mais pessoas? (S/N) '))
    if opc.lower() == 'n':
        break

menores_de_dezoito = {}

for cpf, info in list(pessoas.items()):
    if info['idade'] < 18:
        menores_de_dezoito[cpf] = info
        pessoas.pop(cpf)

print('Maiores de 18:')
print(pessoas)

print('Menores de 18:')
print(menores_de_dezoito)