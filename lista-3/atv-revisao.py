funcionarios = [] #lista de funcionários

def imprimir (lista):
    print("\nFUNCIONÁRIOS:")
    for funcionario in lista:
        print("--------------------------------")
        print(f"Nome: {funcionario['nome']}\nCPF: {funcionario['cpf']}\nCargo: {funcionario['cargo']}\nSalário: {round(funcionario['salario'], 2)}\nTelefones: {funcionario['telefones']}")
        print("--------------------------------")

def cadastroFuncionario (lista):
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))
    telefones = []
    print(f"Digite a quantidade de telefones do funcionário {nome}: ")
    qtd = int(input()) #2
    
    for i in range(qtd):
        print(f"Digite o {i+1}º telefone: ")
        telefone = int(input())
        telefones.append(telefone)

    funcionario = {"nome": nome, "cpf": cpf, "cargo": cargo,"salario": salario,"telefones": telefones}

    funcionarios.append(funcionario)

    print("\nFuncionário cadastrado!")

def pesquisarFuncionario (lista):
    funcionario = research(lista)
    if funcionario:
        print("\nFUNCIONÁRIO:")
        print(f"Nome: {funcionario['nome']}\nCPF: {funcionario['cpf']}\nCargo: {funcionario['cargo']}\nSalário: R$ {round(funcionario['salario'], 2)}\nTelefones: {funcionario['telefones']}")
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

def edit(lista):
        funcionario = research(lista)
        if funcionario:
            print(f"\nAlterar dados do funcionário {funcionario['nome']}")
            funcionario['cargo'] = input('Digite o novo cargo: ')
            funcionario['salario'] = float(input('Digite o novo salário: '))
            funcionario['telefones'].clear()

            print(f"Digite a quantidade de telefones para cadastrar: ")
            qtd = int(input()) #2
    
            for i in range(qtd):
                print(f"Digite o {i+1}º telefone: ")
                telefone = int(input())
                funcionario['telefones'].append(telefone)

            print("\nDados alterados!")
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
        case 4:
            if funcionarios:
                edit(funcionarios)
            else:
                print("\nNão há funcionários cadastrados") 
        case 5:
            if funcionarios:
                deletarFuncionario(funcionarios)
            else:
                print("\nNão há funcionários cadastrados")
        case 6:
            if funcionarios:
                imprimir(funcionarios)
            else:
                print("\nNão há funcionários cadastrados")
        case 0:
            print("\nEncerrando...\n")
            break
        case _:
            print("\nOpção não encontrada!")

