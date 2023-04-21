#biblioteca para gerar strings que não se repetem
import shortuuid

def menu ():
    print("MENU")
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
    verificar_cpf = check_motorista(motoristas, cpf)
    #verifica se o CPF já existe
    if not verificar_cpf:
        rg = int(input("Digite o RG: "))
        cnh = int(input("Digite o CNH: "))
        motorista = {}

        motorista[cpf] = {"nome": nome, "CPF": cpf, "RG": rg, "CNH": cnh, "qtdViagens": 0}

        motoristas.update(motorista) 
        
        print("\nMotorista cadastrado!\n") 
    else:
        print("\nERRO! Já existe um motorista cadastrado com esse CPF\n")
        return 

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
    
    verificar_placa = check_placa(veiculos, placa)
    
    if not verificar_placa:
        chassi = input("Digite o chassi: ")
        cor = input("Digite a cor: ")
        km = float(input("Digite a kilômetragem: "))
        veiculo = {}

        veiculo[placa] = {"marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "chassi": chassi, "cor": cor, "km": km}

        veiculos.update(veiculo)

        print("\nVeículo cadastrado!\n")   
        return
    else:
        print("\nERRO! Já existe um veículo cadastrado com essa placa\n")
    
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
    if distancia <= 0:
        print("\nERRO! a distância não pode ser negativa ou zero!\n")
        return
        
    cpf = int(input("Informe o CPF do motorista: "))
    placa = input("Informe a placa do veículo: ")
    
    motorista = check_motorista(motoristas, cpf)
    veiculo = check_placa(veiculos, placa)
    
    if motorista and veiculo:
        cod = shortuuid.uuid()[:8] #recebe uma string exclusiva de 8 caracteres
        viagem = {}
        viagem[cod] = {"destino": destino, "origem": origem, "distancia": distancia, "motorista": motorista, "veiculo": veiculo}
        
        viagens.update(viagem)
        veiculo['km'] += distancia #atualiza a quilometragem do veiculo a cada registro de viagem
        motorista['qtdViagens'] += 1 #atualiza a qtd de viajens do motorista a cada registro de viagem
        
        print("\nViagem cadastrada!")
        print(f"Código da viagem: {cod}\n")
    else:
        print("\nCPF do motorista ou placa do veículo inválido!\n")

def editar_viagem(viagens, motoristas, veiculos):
    cod = input("Informe código da viagem: ")
    viagem = check_viagem(viagens, cod)
    
    if viagem:
        print("VIAGEM ENCONTRADA")
        cpf = int(input("\nDigite o CPF do novo motorista: "))
        placa = input("Digite a placa do novo veículo: ")
        motorista = check_motorista(motoristas, cpf)
        veiculo = check_placa(veiculos, placa)
    
        if motorista and veiculo:            
            viagem['motorista'] = motorista
            viagem['veiculo'] = veiculo
            
            print("\nViagem alterada com sucesso!\n")

        else:
            print("\nCPF do motorista ou placa do veículo inválido!\n")     
    else:
        print("\nViagem não encontrada!\n")
    
def check_viagem(viagens, cod):
    for chave in viagens:
        if cod == chave:
            return viagens[chave]
    return


def registrar_abastecimento(abastecimentos, veiculos):
    placa = input("\nInforme a placa do veículo que deseja registar o abastecimento: ")
    
    veiculo = check_placa(veiculos, placa)
    
    if veiculo:
        valor = float(input("Digite o valor do abastecimento R$: "))
        data = input("Digite a data no formato dd/mm/aaaa: ")
        quantidade = float(input("Digite a quantidade do abastecimento em L: "))
        
        cod = shortuuid.uuid()[:8] #recebe uma string exclusiva de 8 caracteres
        abastecimento = {}        
        abastecimento[cod] = {"veiculo": veiculo, "valor": valor, "data": data, "quantidade": quantidade}
        
        abastecimentos.update(abastecimento)
        
        print("\nAbastecimento cadastrado!")
        print(f"Código do abastecimento: {cod}\n")
        
    else:
        print("\nVeículo não encontrado!\n")

def registrar_manutencao(manutencoes, veiculos):
    placa = input("Informe a placa do veículo que deseja registar a manutenção: ")
    
    veiculo = check_placa(veiculos, placa)
    
    if veiculo:
        data = input("Digite a data no formato dd/mm/aaaa: ")
        tipo = input("Digite o tipo de manutenção: ")
        custo = float(input("Digite o custo da manutenção R$: "))
        
        cod = shortuuid.uuid()[:8] #recebe uma string exclusiva de 8 caracteres
        manutencao = {}        
        manutencao[cod] = {"veiculo": veiculo, "data": data, "tipo": tipo, "custo": custo}
        
        manutencoes.update(manutencao)
        
        print("\nManutenção cadastrada!")
        print(f"Código da manuteção: {cod}\n")
        
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
    
    
# motoristas = {}    
# veiculos = {}
# viagens = {}
veiculos={"BCC009":{"marca":"Fiat", "modelo":"UNO", "ano":2003, 
                    "placa":"BCC009", "chassi":"36563652", "cor":"Branco","km":500},
         "BCC006":{"marca":"Fiat", "modelo":"Toro", "ano":2003, 
                   "placa":"BCC006", "chassi":"36563652","cor":"Branco","km":500},
         "BCC008":{"marca":"Fiat", "modelo":"Argo", "ano":2003, 
                   "placa":"BCC007", "chassi":"36563652","cor":"Branco","km":500}  }

motoristas={11111:{"nome":"François", "CPF":11111, "RG":223212, "CNH":34221},
            22222:{"nome":"Ana", "CPF":22222, "RG":223212, "CNH":34221},
            33333:{"nome":"Maria", "CPF":33333, "RG":223212, "CNH":"34221"}}

viagens = {
    1: {"destino":"Bacabal", "origem":"Caxias", "distância":200.0, "motorista":motoristas[11111], "veiculo":veiculos["BCC009"]},
    2: {"destino":"Bacabal", "origem":"Caxias", "distância":200.0, "motorista":motoristas[11111], "veiculo":veiculos["BCC009"]},
    3: {"destino":"Bacabal", "origem":"Caxias", "distância":300.0, "motorista":motoristas[33333], "veiculo":veiculos["BCC009"]},
    4: {"destino":"Bacabal", "origem":"Caxias", "distância":100.0, "motorista":motoristas[22222], "veiculo":veiculos["BCC009"]},
    5: {"destino":"Bacabal", "origem":"Caxias", "distância":100.0, "motorista":motoristas[22222], "veiculo":veiculos["BCC009"]},
    6: {"destino":"Bacabal", "origem":"Caxias", "distância":200.0, "motorista":motoristas[11111], "veiculo":veiculos["BCC009"]}



}
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
        # case 7:
        #     qtdViagens(viagens, motoristas)
                    
        case 0:
            print("\nEncerrando...\n")
            break
        case _:
            print("\nOperação inválida!\n")
            