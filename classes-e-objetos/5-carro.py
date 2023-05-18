class Carro:
    quantidade_carros = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

        Carro.quantidade_carros += 1 #para não criar uma variável local
        
carro1 = Carro('Fiat', 'UNO')
carro2 = Carro('Chevrolet', 'UNO')
carro3 = Carro('Fiat', 'Toro')

print(f"Qtd: {Carro.quantidade_carros}")
