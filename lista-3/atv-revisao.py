"""
Criar um sistema de cadastro de funcionários em python que atenda aos seguintes requisitos.

O sistema deverá ter um menu com as seguintes opções do sistema
    1. Cadastro de Funcionários
    2. Pesquisar funcionário
    3. Cadastrar novo telefone
    4. Editar dados do Funcionário
    5. Deletar funcionário
    0. Sair

2. Cada funcionário deverá ser um dicionário com os seguintes atributos (chaves): NOME, CPF, CARGO, SALARIO, TELEFONES.
Onde a chave telefones deve receber uma lista de telefones. Os funcionários (dicionários) deverao ser armazenados em uma 
lista de Funcionários
3. O sistema deve ter uma função para encontra (pesquisar) um funcionário pelo seu cpf e exibir na tela seus dados
4. O sistema deve ter uma função para encontrar um funcionário e adicionar um novo telefone
5. O sistema deve ter uma função capaz de encontar um funcionário e editar seus dados
6. O sistema deve ter uma função para deletar um funcionário
7. Caso nao exista um funcionário o sistema nao devera executar as opções 2, 3, 4 e 5
"""

funcionarios = [] #lista de funcionários

def imprimir (lista):
    print("\nFuncionários:\n")
    for  funcionario in lista:
        print(f"Nome: {funcionario['nome']} - CPF: {funcionario['cpf']}")

def cadastroFuncionario (lista):
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))
    telefones = []
    print(f"Digite a quantidade de telefone do funcionário {nome}: ")
    qtd = int(input()) #2
    
    for i in range(qtd):
        print(f"Digite o {i+1}º telefone: ")
        telefone = int(input())
        telefones.append(telefone)

    funcionario = {"nome": nome, "cpf": cpf, "telefones": telefones}

    funcionarios.append(funcionario)

def pesquisarFuncionario (lista):
    funcionario = research(lista)
    if funcionario:
        print(f"Nome: {funcionario['nome']}\nCPF: {funcionario['cpf']}\nTelefones: {funcionario['telefones']}")
    else:
        print("\nCPF não encontrado!")

def deletarFuncionario (lista):
    funcionario = research(lista)
    if funcionario:
        lista.remove(funcionario)
        print("\nFuncionário deletado!")
    else:
        print("\nCPF não encontrado!")

def research (lista):
    cpf = int(input("Digite o CPF: "))
    for funcionario in lista:
        if cpf == funcionario['cpf']:
            return funcionario
    return 

def addNewPhone (lista):
    funcionario = research(lista)
    if funcionario:
        print(f"Digite um novo telefone para o funcionário {funcionario['nome']}: ")
        telefone = int(input())

        funcionario['telefones'].append(telefone)
        print("\nNovo telefone cadastrado!")
    else:
        print("\nCPF não encontrado!")

def menu ():
    print("\nMENU")
    print("1. Cadastro de Funcionários")
    print("2. Pesquisar funcionário")
    print("3. Cadastrar novo telefone")
    print("4. Editar dados do Funcionário")
    print("5. Deletar funcionário")
    print("6. Mostrar todos os funcionários (extra)")
    print("0. Sair")
    
    print("\nInforme a opção: ")

while True:
    menu()
    opc = int(input())

    match opc:
        case 1:
            cadastroFuncionario(funcionarios)
        case 2:
            if funcionarios:
                pesquisarFuncionario(funcionarios)
            else:
                print("\nNão há funcionários cadastrados")   
        case 3:
            if funcionarios:
                addNewPhone(funcionarios)
            else:
                print("\nNão há funcionários cadastrados")         
        case 5:
            if funcionarios:
                deletarFuncionario(funcionarios)
            else:
                print("\nNão há funcionários cadastrados")
        case 0:
            print("\nEncerrando...\n")
            break
        case _:
            print("\nOpção não encontrada!\n")

