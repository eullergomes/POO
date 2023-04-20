def menu ():
    print("\nMENU")
    print("1. Gerencimento de Motoristas")
    print("2. Gerencimento de Veículos")
    print("3. Gerencimento de Viagem")
    print("4. Registrar Abastecimento")
    print("5. Registrar Manutenção")
    print("6. Relatório")
    print("0. Sair")
    print("\nInforme a opção: ")
    
def menuMotoristas():
    print("O que você gostaria de fazer?")
    print("1. Cadastrar Novo Motorista")
    print("2. Pesquisar Motorista")
    print("3. Editar Motorista")
    print("4. Deletar Motorista")
    print("5. Imprimir Motoristas")
    print("\nInforme opção: ")

#cadastrar novo motorista
def cadastro_motorista (motoristas):
    nome = input("Digite o nome: ")
    cpf = int(input("Digite o CPF: "))
    rg = int(input("Digite o RG: "))
    cnh = int(input("Digite o CNH: "))
    motorista = {}

    motorista[cpf] = {"nome": nome, "CPF": cpf, "RG": rg, "CNH": cnh}

    motoristas.update(motorista)

    print("\nMotorista cadastrado!\n")    

#imprime o motorista pesquisado
def pesquisar_motorista (motoristas):
    cpf = int(input('Informe o CPF: '))
    motorista = check_motorista(motoristas, cpf)
    if motorista:
        print("\nMOTORISTA:")
        print(f"Nome: {motorista['nome']}")
        print(f"CPF: {motorista['CPF']}")
        print(f"RG: {motorista['RG']}")
        print(f"CNH: {motorista['CNH']}\n")
    else:
        print("\nCPF não encontrado!\n")

#retorna o dic do motorista
def check_motorista(motoristas, cpf):
    for chave in motoristas:
        if cpf == chave:
            return motoristas[chave]
    return

#edita um determinado motorista
def editar_motorista(motoristas):
    cpf = int(input('Informe o CPF: '))
    motorista = check_motorista(motoristas, cpf)
    if motorista:
        print(f"\nAlterar dados {motorista['nome']}")
            
        motorista['RG'] = int(input('Digite o novo RG: '))
        motorista['CNH'] = int(input('Digite o novo CNH: '))

        print("\nDados alterados!\n")
    else:
        print("\nCPF não encontrado!\n")

#deleta um determinado motorista
def deletarMotorista (motoristas):
    cpf = int(input('Informe o CPF: '))
    motorista = check_motorista(motoristas, cpf)
    if motorista:
        del motoristas[cpf]
        print("\nMotorista deletado!\n")
    else:
        print("\nCPF não encontrado!\n")

#imprime os motoristas cadastrados
def imprimirMotoristas (motoristas):
    print("\nMOTORISTAS:")
    for motorista in motoristas.values():
        print("--------------------------------")
        print(f"Nome: {motorista['nome']}")
        print(f"CPF: {motorista['CPF']}")
        print(f"RG: {motorista['RG']}")
        print(f"CNH: {motorista['CNH']}")
        print("--------------------------------")
    
    
def menuVeiculos():
    print("O que você gostaria de fazer?")
    print("1. Cadastrar Veículo")
    print("2. Pesquisar Veículo")
    print("3. Editar Editar veículo")
    print("4. Deletar Veículo")
    print("5. Ver quilometragem do Veículo")
    print("\nInforme opção: ")

#cadastrar novo veículo
def cadastroVeiculo (veiculos):
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))
    placa = input("Digite a placa: ")
    chassi = input("Digite o chassi: ")
    cor = input("Digite a cor: ")
    km = float(input("Digite a kilômetragem: "))
    veiculo = {}

    veiculo[placa] = {"marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "chassi": chassi, "cor": cor, "km": km}

    veiculos.update(veiculo)

    print("\nVeículo cadastrado!")   
    
#imprime o veículo pesquisado
def pesquisarVeiculo (veiculos):
    placa = input('Informe a placa: ')
    veiculo = check_placa(veiculos, placa)
    if veiculo:
        print("\nVEÍCULO:")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Placa: {veiculo['placa']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Kilômetria: {veiculo['km']} km\n")
    else:
        print("\nPlaca não encontrada!\n")

#edita dados de um veículo   
def editarVeiculo(veiculos):
    placa = input('Informe a placa: ')
    veiculo = check_placa(veiculos, placa)
    if veiculo:
        print(f"\nAlterar dados do carro de placa {veiculo['placa']}")
            
        veiculo['chassi'] = input('Digite o novo chassi: ')
        veiculo['cor'] = input('Digite a nova cor: ')

        print("\nDados alterados!\n")
    else:
        print("\nPlaca não encontrada!\n")

#retorna o veiculo pesquisado
def check_placa(veiculos, placa):
    for chave in veiculos:
        if placa == chave:
            return veiculos[chave]
    return

#deleta um veículo
def deletarVeiculo (veiculo):
    placa = input('Informe a placa: ')
    motorista = check_placa(veiculo, placa)
    if motorista:
        del veiculo[placa]
        print("\nVeiculo deletado!\n")
    else:
        print("\nCPF não encontrado!\n")

def imprimirVeiculos (veiculos):
    print("\nVEICULOS:")
    for veiculo in veiculos.values():
        print("--------------------------------")
        print(f"Marca: {veiculo['marca']}")
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}")
        print(f"Placa: {veiculo['placa']}")
        print(f"Chassi: {veiculo['chassi']}")
        print(f"Cor: {veiculo['cor']}")
        print(f"Quilometragem: {veiculo['km']}")
        print("--------------------------------")


def menuViagem():
    print("1. Cadastrar Viagem")
    print("2. Editar Viagem")
    print("\nInforme a opção: ")
    
def cadastrar_viagem(viagens, motoristas, veiculos):
    destino = input("Informe o destino: ")
    origem = input("Informe a origem: ")
    distancia = float(input("Informe a distância em KM: "))
    cpf = int(input("Informe o CPF do motorista: "))
    placa = input("Informe a placa do veículo: ")
    
    motorista = check_motorista(motoristas, cpf)
    veiculo = check_placa(veiculos, placa)
    
    if motorista and veiculo:
        id = input("Informe uma ID para a viagem (exclusiva): ")
        viagem = {}
        viagem[id] = {"destino": destino, "origem": origem, "distancia": distancia, "motorista": motorista, "veiculo": veiculo}
        
        viagens.update(viagem)
        
        print("\nViagem cadastrada!\n")
    else:
        print("\nCPF do motorista ou placa do veículo inválido!\n")

def editar_viagem(viagens, motoristas, veiculos):
    id = input("Informe o ID da viagem: ")
    viagem = check_viagem(viagens, id)
    
    if viagem:
        cpf = int(input("Digite um novo CPF de motorista: "))
        placa = input("Digite uma nova placa de veículo: ")
        motorista = check_motorista(motoristas, cpf)
        veiculo = check_placa(veiculos, placa)
        
        if motorista and veiculo:
            viagem['destino'] = input("Digite o novo destino: ")
            viagem['origem'] = input("Digite a nova origem: ")
            viagem['distancia'] = input("Digite a nova distância: ")
            viagem['motorista'] = motorista
            viagem['veiculo'] = veiculo
            
            print("\nViagem alterada com sucesso!\n")
        else:
            print("\nCPF do motorista ou placa do veículo inválido!\n")     
    else:
        print("\nViagem não encontrada!\n")
    
def check_viagem(viagens, id):
    for chave in viagens:
        if id == chave:
            return viagens[chave]
    return


def registrar_abastecimento(abastecimentos, veiculos):
    placa = input("\nInforme a placa do veículo que deseja registar o abastecimento: ")
    
    veiculo = check_placa(veiculos, placa)
    
    if veiculo:
        valor = float(input("Digite o valor do abastecimento R$: "))
        data = input("Digite a data no formato dd/mm/aaaa: ")
        quantidade = float(input("Digite a quantidade do abastecimento em L: "))
        
        abastecimento = {}        
        abastecimento[placa] = {"veiculo": veiculo, "valor": valor, "data": data, "quantidade": quantidade}
        
        abastecimentos.update(abastecimento)
        
        print("\nAbastecimento cadastrado!\n")
        
        
    else:
        print("\nVeículo não encontrado!\n")

def registrar_manutencao(manutencoes, veiculos):
    placa = input("Informe a placa do veículo que deseja registar a manutenção: ")
    
    veiculo = check_placa(veiculos, placa)
    
    if veiculo:
        data = input("Digite a data no formato dd/mm/aaaa: ")
        tipo = input("Digite o tipo de manutenção: ")
        custo = float(input("Digite o custo da manutenção R$: "))
        
        manutencao = {}        
        manutencao[placa] = {"veiculo": veiculo, "data": data, "tipo": tipo, "custo": custo}
        
        manutencoes.update(manutencao)
        
        print("\nManutenção cadastrada!\n")
        
        
    else:
        print("\nVeículo não encontrado!\n")

def relatorio (veiculos, motoristas, viagens, abastecimentos, manutencoes):
    print("RELATÓRIO:\n")
    print("Veículos")
    print(veiculos)
    
    print("\nMotoristas:")
    print(motoristas)
    
    print("\nViagens:")
    print(viagens)
    
    print("\nAbastecimentos:")
    print(abastecimentos)
    
    print("\nManutenções:")
    print(manutencoes)
    
    
motoristas = {}    
veiculos = {}
viagens = {}
abastecimentos = {}
manutencoes = {}

while True:
    menu()
    opc = int(input())
    
    match opc:
        case 1:
            menuMotoristas()
            opc2 = int(input())
            match opc2:
                case 1:
                    cadastro_motorista(motoristas)
                case 2:
                    if motoristas:
                        pesquisar_motorista(motoristas)
                    else:
                        print("\nNão há motoristas cadastrados!\n")
                case 3:
                    if motoristas:
                        editar_motorista(motoristas)
                    else:
                        print("\nNão há motoristas cadastrados!\n")
                case 4:
                    if motoristas:
                        deletarMotorista(motoristas)
                    else:
                        print("\nNão há motoristas cadastrados!\n")
                case 5:
                    if motoristas:
                        imprimirMotoristas(motoristas)
                    else:
                        print("\nNão há motoristas cadastrados!\n")
                case _:
                    print("\nOperação inválida!\n")
        
        case 2:
            menuVeiculos()
            opc2 = int(input())
            match opc2:
                case 1:
                    cadastroVeiculo(veiculos)
                case 2:
                    if veiculos:
                        pesquisarVeiculo(veiculos)
                    else:
                        print("\nNão há veículos cadastrados!\n")
                case 3:
                    if veiculos:
                        editarVeiculo(veiculos)
                    else:
                        print("\nNão há veículos cadastrados!\n")
                case 4:
                    if veiculos:
                        deletarVeiculo(veiculos)
                    else:
                        print("\nNão há veículos cadastrados!\n")
                case 5:
                    if veiculos:
                        imprimirVeiculos(veiculos)
                    else:
                        print("\nNão há veículos cadastrados!\n")
                case _:
                    print("\nOperação inválida!\n")
                   
        case 3:
            menuViagem()
            opc2 = int(input())
            match opc2:
                case 1:
                    if motoristas and veiculos:
                        cadastrar_viagem(viagens, motoristas, veiculos)
                    else:
                        print("\nNão há motoristas ou veículos cadastrados!\n")
                case 2:
                    if viagens:
                        editar_viagem(viagens, motoristas, veiculos)
                    else:
                        print("\nNão há viagens cadastradas!\n")

        case 4:
            if veiculos:
                registrar_abastecimento(abastecimentos, veiculos)
            else:
                print("\nNão há veículos cadastrados!\n")
            
        case 5:
            if veiculos:
                registrar_manutencao(manutencoes, veiculos)
            else:
                print("\nNão há veículos cadastrados!\n")
            
        case 6:
            if veiculos or motoristas or viagens or abastecimentos or manutencoes:
                relatorio(veiculos, motoristas, viagens, abastecimentos, manutencoes)
            else:
                print("\nNão há nada cadastrado!\n")
                    
        case 0:
            print("\nEncerrando...\n")
            break
        case _:
            print("\nOperação inválida!\n")
            