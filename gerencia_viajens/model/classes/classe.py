# from interface import FormasInterface

class Motorista:
    def __init__(self, nome: str, cpf: str, rg: str, cnh: str, qtdViagens: int, km: float) -> None:
        self.nome = nome
        self.cpf = cpf 
        self.rg = rg
        self.cnh = cnh
        self.qtdViagens = qtdViagens
        self.km = km
        
class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: str, placa: str, chassi: str, cor: str, km: float, abastecimento: float, manutencao: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.chassi = chassi
        self.cor = cor
        self.km = km
        self.abastecimento = abastecimento
        self.manutencao = manutencao
        
class Viagem:
    def __init__(self, destino: str, origem: str, distancia: float, cod: str, motorista: object, veiculo: object) -> None:
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
        self.cod = cod
    

class Abastecimento:
    def __init__(self, veiculo: object, valor: float, data: str, quantidade: float, cod: str) -> None:
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade
        self.cod = cod

class Manutencoes:
    def __init__(self, veiculo: object, data: str, tipo: str, custo: float, cod: str) -> None:
        self.veiculo = veiculo
        self.data = data
        self.tipo = tipo
        self.custo = custo
        self.cod = cod
    
