from .interface import ManagerInterface
from .classe import Motorista, Veiculo, Viagem, Abastecimento, Manutencoes
import json
import shortuuid #biblioteca para gerar strings que não se repetem (cód. da viagem)

def check_dados_motorista(nome: str, rg: str, cnh: str, cpf = 'padrao'):
    if not nome.strip() or not cpf.strip() or not cnh or not rg.strip():
        raise ValueError("Ausencia de dado(s)")

def novo_motorista():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    cnh = input("CNH: ")
    qtdViagens = 0
    km = 0
    print()
    
    check_dados_motorista(nome, rg, cnh, cpf)

    return Motorista(nome, cpf, rg, cnh, qtdViagens, km)

def nova_viagem(motoristas: object, veiculos: object):
    destino = input("Informe o destino: ")
    origem = input("Informe a origem: ")
    
    distancia = float(input("Informe a distância em KM: "))
    if distancia <= 0:
        raise ValueError("a distância não pode ser negativa ou zero")
        
    cpf = input("Informe o CPF do motorista: ")
    placa = input("Informe a placa do veículo: ")
    
    motorista = motoristas.check(cpf)
    veiculo = veiculos.check(placa)
    
    if motorista and veiculo:
        motorista["qtdViagens"] =+ 1
        cod = shortuuid.uuid()[:4] #recebe uma string exclusiva de 4 caracteres
        return Viagem(destino, origem, distancia, cod, motorista, veiculo)
    else:
        raise ValueError("CPF ou placa não encontrado")

def check_dados_veiculo(chassi: str, cor: str, marca = "padrao", modelo = "padrao", ano = "padrao"):
    if not marca.strip() or not modelo.strip() or not ano.strip() or not chassi.strip() or not cor.strip():
        raise ValueError("Ausencia de dado(s)")
        
def novo_veiculo():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    placa = input("Placa: ")
    chassi = input("Chassi: ")
    cor = input("Cor: ")
    km = float(input("Quilometragem: "))
    abastecimento = 0
    manutencao = 0
    
    print()
    
    check_dados_veiculo(chassi, cor, marca, modelo, ano)
    
    return Veiculo(marca, modelo, ano, placa, chassi, cor, km, abastecimento, manutencao)

def nova_manutecao(veiculos):
    placa = input("Informe a placa do veículo que deseja registar a manutenção: ")
    
    veiculo = veiculos.check(placa)
    
    if veiculo:
        data = input("Data (dd/mm/aaaa): ")
        tipo = input("Tipo: ")
        custo = float(input("Custo: R$ "))
        
        veiculo['manutencao'] += custo
                
        cod = shortuuid.uuid()[:4] #recebe uma string exclusiva de 4 caracteres
    
        return Manutencoes(veiculo, data, tipo, custo, cod)
    else:
        raise ValueError("veículo não encontrado")
    
def novo_abastecimento(veiculos):
    placa = input("Informe a placa do veículo que deseja registar o abastecimento: ")
    
    veiculo = veiculos.check(placa)
    
    if veiculo:
        valor = float(input("Valor: R$ "))
        data = input("Data (dd/mm/aaaa): ")
        quantidade = float(input("Digite a quantidade do abastecimento em L: "))
        
        veiculo['abastecimento'] += valor
            
        cod = shortuuid.uuid()[:4] #recebe uma string exclusiva de 4 caracteres
    
        return Abastecimento(veiculo, valor, data, quantidade, cod)
    else:
        raise ValueError("veículo não encontrado")

class Manager_motorista(ManagerInterface):
    motoristas = {}
    # motoristas = {
    #     "11111": {"nome": "François", "cpf": "11111", "rg": "223212", "cnh": "34221", "qtdViagens": 0, "km": 40},
    #     "22222": {"nome": "Ana", "cpf": "22222", "rg": "223212", "cnh": "34221", "qtdViagens": 0, "km": 600},
    #     "33333": {"nome": "MAria", "cpf": "33333", "rg": "223212", "cnh": "34221", "qtdViagens": 0, "km": 100}
    # }
    
    def cadastrar(self):
        try:
            motorista = novo_motorista()
            if motorista.cpf in self.motoristas:
                print("Erro: motorista já cadastrado")
                return
        
        except ValueError as e:
            print(f"Erro: {str(e)}")
        
        else:
            self.motoristas[motorista.cpf] = motorista.__dict__
            self.salvar_arq()
            print("Motorista cadastrado")            
    
    def remover(self, cpf: str):
        if cpf not in self.motoristas:
            print("Motorista não encontrado")
            return
        del self.motoristas[cpf]
        self.salvar_arq()
        print("Motorista removido")
    
    def editar(self):
        cpf = input("CPF: ")
        if cpf not in self.motoristas:
            print("Motorista não encontrado")
            return
        
        try:
            nome = input("Nome: ")
            rg = input("RG: ")
            cnh = input("CNH: ")
        
            check_dados_motorista(nome, rg, cnh)
            
        except ValueError as e:
            print(f"Erro: {str(e)}")

        else:
        
            self.motoristas[cpf]['nome'] = nome

            self.motoristas[cpf]['rg'] = rg
            
            self.salvar_arq()
        
            print("\nDados alterados")
    
    def check(self, cpf: str):
        if cpf in self.motoristas:
            return self.motoristas[cpf]
            
    def pesquisar(self):
        cpf = input("\nCPF: ")
        
        motorista = self.check(cpf)
        
        if motorista:
            print("\nMOTORISTA:")
            print(f"Nome: {motorista['nome']}")
            print(f"CPF: {motorista['cpf']}")
            print(f"RG: {motorista['rg']}")
            print(f"CNH: {motorista['cnh']}")
            print(f"Qtd de viagens: {motorista['qtdViagens']}")
            print(f"Quilômetros percorridos: {motorista['km']}\n")
        else:
            print("\nCPF não encontrado!\n")
    
    def salvar_arq(self):
        with open("motoristas.json", 'w') as f:
            json.dump(self.motoristas, f)
    
    def carregar_arq(self):
        try:
            with open("motoristas.json", 'r') as f:
                self.motoristas = json.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")
    
    def maior_motorista_km (self):
        motorista = {}
        maior = float('-inf')
        for cpf in self.motoristas:
            if self.motoristas[cpf]['km'] > maior:
                maior = self.motoristas[cpf]['km']
                motorista = self.motoristas[cpf]
        return motorista

class Manager_veiculo(ManagerInterface):
    veiculos = {}
    # veiculos = {
    #     "BCC009": {"marca": "Fiat", "modelo": "UNO", "ano": "2003", "placa": "BCC009", "chassi": "36563652", "cor": "Branco", "km": 260, "abastecimento": 200.95, "manutencao": 1200.0},
    #     "BCC006": {"marca": "Fiat", "modelo": "Toro", "ano": "2003", "placa": "BCC006", "chassi": "36563652", "cor": "Branco", "km": 500, "abastecimento": 3000, "manutencao": 800.0},
    #     "BCC008": {"marca": "Fiat", "modelo": "Argo", "ano": "2003", "placa": "BCC007", "chassi": "36563652", "cor": "Branco", "km": 170.6, "abastecimento": 187.25, "manutencao": 900.0}
    # }   
    
    def cadastrar(self):
        try:
            veiculo = novo_veiculo()
            if veiculo.placa in self.veiculos:
                print("\nErro! Veículo já cadastrado")
                return
        except ValueError as e:
            print(f"Erro: {str(e)}")
        else:
            self.veiculos[veiculo.placa] = veiculo.__dict__
            self.salvar_arq()
            print("Veiculo cadastrado")
        
    def remover(self, placa: str):        
        if placa not in self.veiculos:
            print("\nVeículo não encontrado")
            return
        del self.veiculos[placa]
        
        print("\nVeiculo removido\n")
    
    def editar(self):
        placa = input("Placa: ")
        if placa not in self.veiculos:
            print("\nVeículo não encontrado")
            return
        
        try:    
            chassi = input("Chassi: ")
            cor = input("Cor: ")
            
            check_dados_veiculo(chassi, cor)
        
        except ValueError as e:
            print(f"Erro: {str(e)}")
            
        else:
            self.veiculos[placa]['chassi'] = chassi
        
            self.veiculos[placa]['cor'] = cor
            
            self.salvar_arq()
        
            print("\nDados alterados")
    
    def check(self, placa: str):
        if placa in self.veiculos:
            return self.veiculos[placa]
    
    def pesquisar(self):
        placa = input('\nInforme a placa: ')
        
        veiculo = self.check(placa)
        
        if veiculo:
            print("\nVEICULO:")
            print(f"Marca: {veiculo['marca']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Ano: {veiculo['ano']}")
            print(f"Placa: {veiculo['placa']}")
            print(f"Chassi: {veiculo['chassi']}")
            print(f"Cor: {veiculo['cor']}")
            print(f"Quilometragem: {veiculo['km']} km")
            print(f"Total de abastecimetos: R$ {veiculo['abastecimento']}")
            print(f"Total de manuteções: R$ {veiculo['manutencao']}\n")
        else:
            print("\nPlaca não encontrada\n")
            
    def salvar_arq(self):
        with open('veiculos.json', 'w') as f:
            json.dump(self.veiculos, f)
    
    def carregar_arq(self):
        try:
            with open('veiculos.json', 'r') as f:
                self.veiculos = json.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")
            
    def maior_veiculo_km (self):
        veiculo = {}
        maior = float('-inf')
        for placa in self.veiculos:
            if self.veiculos[placa]['km'] > maior:
                maior = self.veiculos[placa]['km']
                veiculo = self.veiculos[placa]
        return veiculo

    def total_abastecimento (self):
        despesa = 0.0
        for placa in self.veiculos:
            despesa += self.veiculos[placa]['abastecimento']
        return despesa
    
    def total_manutencao (self):
        despesa = 0.0
        for placa in self.veiculos:
            despesa += self.veiculos[placa]['manutencao']
        return despesa
            
class Manager_viagem():
    viagens = {}
    
    def cadastrar(self, motoristas: object, veiculos: object):
        try:
            viagem = nova_viagem(motoristas, veiculos)
            
        except ValueError as e:
            print(f"\nErro: {str(e)}\n")
            
        else:
            self.viagens[viagem.cod] = viagem.__dict__
            self.salvar_arq()
            print("\nViagem cadastrada\n")
            print(f"\nCódigo da viagem: {viagem.cod}\n")
            
    def editar(self, motoristas: object, veiculos: object):        
        cod = input("Informe o código da viagem: ")
        
        viagem = self.check(cod)
        
        if viagem:
            print("\nVIAGEM ENCONTRADA")
            cpf = input("\nInforme o CPF do novo motorista: ")
            placa = input("Informe a placa do novo veículo: ")
            
            motorista = motoristas.check(cpf)
            veiculo = veiculos.check(placa)
            
            if motorista and veiculo:
                viagem['motorista']['qtdViagens'] -= 1
                viagem['motorista'] = motorista
                viagem['motorista']['qtdViagens'] += 1
                viagem['veiculo'] = veiculo
            
                self.salvar_arq()
                print("\nViagem alterada com sucesso!\n")
            else:
                print("\nErro: CPF do motorista ou placa do veículo inválido\n") 
        else:
            print("\nErro: viagem não encontrada\n")
        
    def check(self, cod: str):
        if cod in self.viagens:
            return self.viagens[cod]
    
    def salvar_arq(self):
        with open("viagens.json", 'w') as f:
            json.dump(self.viagens, f)
    
    def carregar_arq(self):
        try:
            with open("viagens.json", 'r') as f:
                self.viagens = json.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")

class ServiceAbastecimento():
    abastecimentos = {}
    
    def registrar(self, veiculos: object):
        try:
            abastecimento = novo_abastecimento(veiculos)      
        except ValueError as e:
            print(f"\nErro: {str(e)}\n")       
        else:
            self.abastecimentos[abastecimento.cod] = abastecimento.__dict__
            self.salvar_arq()
            print("\nAbastecimento cadastrado\n")
            print(f"\nCódigo do abastecimento: {abastecimento.cod}\n")
    
    def salvar_arq(self):
        with open('abastecimentos.json', 'w') as f:
            json.dump(self.abastecimentos, f)
    
    def carregar_arq(self):
        try:
            with open('abastecimentos.json', 'r') as f:
                self.abastecimentos = json.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")

class ServiceManutencao():
    manutencoes = {}
    
    def registrar(self, veiculos: object):
        try:
            manutencao = nova_manutecao(veiculos)      
        except ValueError as e:
            print(f"\nErro: {str(e)}\n")       
        else:
            self.manutencoes[manutencao.cod] = manutencao.__dict__
            self.salvar_arq()
            print("\nManutenção cadastrada")
            print(f"\nCódigo da manutenção: {manutencao.cod}\n")
    
    def salvar_arq(self):
        with open('manutencoes.json', 'w') as f:
            json.dump(self.manutencoes, f)
    
    def carregar_arq(self):
        try:
            with open('manutencoes.json', 'r') as f:
                self.manutencoes = json.load(f)
        except FileNotFoundError:
            print("Arquivo não encontrado")


