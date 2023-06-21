from view.menus import *
from model.classes.manager import Manager_motorista, Manager_veiculo, Manager_viagem, ServiceAbastecimento, ServiceManutencao

motorista = Manager_motorista()
veiculo = Manager_veiculo()
viagem = Manager_viagem()
abastecimento = ServiceAbastecimento()
manutencao = ServiceManutencao()

while True:
    print("\nMENU:")
    print("1. Gerenciamento de Motoristas")
    print("2. Gerenciamento de Veiculos")
    print("3. Gerenciamento de Viagens")
    print("4. Registrar abastecimento")
    print("5. Registrar manutenção")
    print("6. Relatório")
    print("0. Encerrar programa")
    op = input("\nInforme a opção: ")
    if op == "1":
        motorista_menu(motorista)
    elif op == "2":
        veiculo_menu(veiculo)
    elif op == "3":
        viagem_menu(viagem, motorista, veiculo)
    elif op == "4":
        reg_abastecimento(abastecimento, veiculo)
    elif op == "5":
        reg_manutencao(manutencao, veiculo)
    elif op == "6":
        relatorio(motorista, veiculo)
    elif op == "0":
        break
    else:
        print("\nOpção inválida - tente novamente")