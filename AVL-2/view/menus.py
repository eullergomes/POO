def motorista_menu(motorista: object):
    while True:
        print("\nMENU - motoristas")
        print("1. cadastrar")
        print("2. remover")
        print("3. editar")
        print("4. pesquisar")
        print("0. voltar")
        op = input("\nInforme a opção: ")
        if op == "1":
            motorista.cadastrar()
        elif op == "2":
            cpf = input("CPF: ")
            motorista.remover(cpf)
        elif op == "3":
            motorista.editar()
        elif op == "4":
            motorista.pesquisar()
        elif op == "0":
            break
        else:
            print("\nOpção inválida - tente novamente")

def veiculo_menu(veiculo: object):
    while True:
        print("\nMENU - veiculos")
        print("1. cadastrar")
        print("2. remover")
        print("3. editar")
        print("4. pesquisar")
        print("0. voltar")
        opc = input("\nInforme a opção: ")
        if opc == "1":
            veiculo.cadastrar()
        elif opc == "2":
            placa = input("Placa: ")
            veiculo.remover(placa)
        elif opc == "3":
            veiculo.editar()
        elif opc == "4":
            veiculo.pesquisar()
        elif opc == "0":
            break
        else:
            print("\nOpção inválida - tente novamente")
        
def viagem_menu(viagem: object, motorista: object, veiculo: object):
    while True:
        print("\nMENU - viagens:")
        print("1. Cadastrar viagem")
        print("2. Editar viagem")
        print("0. Voltar")
        
        opc = input("\nInforme a opção: ")
        
        if opc == "1":
            if len(motorista.motoristas) > 0 and len(veiculo.veiculos) > 0:
                viagem.cadastrar(motorista, veiculo)
            else:
                print("\nErro: não há motoristas ou veículos cadastrados!\n")
                
        elif opc == "2":
            if len(motorista.motoristas) > 0 and len(veiculo.veiculos) > 0:
                viagem.editar(motorista, veiculo)
            else:
                print("\nErro: não há motoristas ou veículos cadastrados!\n")
                
        elif opc == "0":
            break 
        else:
            print("\nOpção inválida - tente novamente")
            
        
def reg_abastecimento(abastecimento: object, veiculo: object):
    if len(veiculo.veiculos) > 0:
        abastecimento.registrar(veiculo)
    else:
        print("\nErro: não há veículos cadastrados!\n")
    
def reg_manutencao(abastecimento: object, veiculo: object):
    if len(veiculo.veiculos) > 0:
        abastecimento.registrar(veiculo)
    else:
        print("\nErro: não há veículos cadastrados!\n")
    
def relatorio(motorista: object, veiculo: object):
    if len(motorista.motoristas) > 0 and len(veiculo.veiculos) > 0:
        print("\nRELATÓRIO:")
        print(f"Quantidade de motoristas: {len(motorista.motoristas)}")
        print(f"Quantidade de veículos: {len(veiculo.veiculos)}")

        motorista_km = motorista.maior_motorista_km()
        print(f"Motorista com maior distância percorrida: {motorista_km['nome']}  /  distância percorrida: {motorista_km['km']} km")
    
        veiculo_km = veiculo.maior_veiculo_km()
        print(f"Veículo com maior quilometragem: {veiculo_km['marca']} - {veiculo_km['modelo']}  /  Distância percorrida: {veiculo_km['km']} km")
    
        print(f"Total de despesas com abastecimento: R$ {veiculo.total_abastecimento()}")
        print(f"Total de despesas com manutenção: R$ {veiculo.total_manutencao()}\n")
    else:   
        print("\nErro: não há motoristas ou veículos cadastrados!\n")
        