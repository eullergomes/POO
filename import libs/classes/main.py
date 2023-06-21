from minha_classe import * #classe
from minha_classe import pessoas, veiculos #dict
from minha_classe import imprimir_pessoas, imprimir_veiculos #função


pessoaA = Pessoa("Euller", 19)
pessoaB = Pessoa("Joao", 22)

pessoaA.cadastro(pessoas)
pessoaB.cadastro(pessoas)

veiculoA = Veiculo('Moto', 2012)
veiculoB = Veiculo('Carro', 2022)

veiculoA.cadastro(veiculos)
veiculoB.cadastro(veiculos)

print("PESSOAS")
imprimir_pessoas(pessoas)

print("VEÍCULOS")
imprimir_veiculos(veiculos)
