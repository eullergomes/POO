class Pessoa:
    indice = 0
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        Pessoa.indice += 1
        self.indice = Pessoa.indice
        
    def cadastro (self, pessoas: dict):
        pessoa = {}
        pessoa[self.indice] = {'nome': self.nome, 'idade': self.idade}
        pessoas.update(pessoa)

class Veiculo:
    indice = 0
    def __init__(self, modelo: str, ano: int) -> None:
        self.modelo = modelo
        self.ano = ano
        Veiculo.indice += 1
        self.indice = Veiculo.indice
        
    def cadastro (self, veiculos: dict):
        veiculo = {}
        veiculo[self.indice] = {'modelo': self.modelo, 'ano': self.ano}
        veiculos.update(veiculo)

def imprimir_pessoas(pessoas: dict):
    for pessoa in pessoas.values():
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}\n")
        
def imprimir_veiculos(veiculos: dict):
    for veiculo in veiculos.values():
        print(f"Modelo: {veiculo['modelo']}")
        print(f"Ano: {veiculo['ano']}\n")

pessoas = {}
veiculos = {}

pessoaA = Pessoa("Euller", 19)
pessoaB = Pessoa("Joao", 22)

pessoaA.cadastro(pessoas)
pessoaB.cadastro(pessoas)

veiculoA = Veiculo('Moto', 2012)
veiculoB = Veiculo('Carro', 2022)

# print("PESSOAS")
# imprimir_pessoas(pessoas)

imprimir_veiculos(veiculos)
# print("VEÍCULOS")
