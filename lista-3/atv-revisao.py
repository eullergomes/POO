"""
Criar um sistema de cadastro de funcionários em python que atenda aos seguintes requisitos.

    1. O sistema deverá ter um menu com as seguintes opções do sistema
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

def inserirFuncionarios (lista, dados):
    lista.append(dados)


def imprimir (lista):
    print("\nFuncionários:\n")
    for  funcionario in lista:
        print(f"Nome: {funcionario['nome']} - CPF: {funcionario['cpf']}")

def cadastroFuncionario ():
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))

    funcionario = {"nome": nome, "cpf": cpf}

    funcionarios.append(funcionario)

def pesquisarFuncionario (lista):
    cpf = int(input("Digite o CPF: "))

    for funcionario in lista:
        if cpf == funcionario['cpf']:
            imprimir(lista)

def deletarFuncionario (lista):
    cpf = int(input("Digite o CPF: "))

    for funcionario in lista:
        if cpf == funcionario['cpf']:
            del funcionario
    print("\nFuncionário deletado com sucesso!\n")

def menu ():
    print("MENU")
    print("1. Cadastro de Funcionários")
    print("2. Pesquisar funcionário")
    print("3. Cadastrar novo telefone")
    print("4. Editar dados do Funcionário")
    print("5. Deletar funcionário")
    print("0. Sair")
    
    print("\nInforme a opção: ")

while True:
    menu()
    opc = int(input())

    match opc:
        case 1:
            cadastroFuncionario()
        case 2:
            imprimir(funcionarios)
        case 3:
            pesquisarFuncionario(funcionarios)
        case 4:
            deletarFuncionario(funcionarios)
        case 0:
            print("\nEcerrando...\n")
            break

    opc = input("\nDeseja continuar o programa? (S/N) ")
    if opc.lower() == 'n':
        print("\nEcerrando...\n")
        break
        
def menu():
    print("MENU")
    print("1. Cadastro de Funcionários")
    print("2. Pesquisar funcionário")
    print("3. Cadastrar novo telefone")
    print("4. Editar dados do Funcionário")
    print("5. Deletar funcionário")
    print("0. Sair")
    print("\nInforme a opção: ")
