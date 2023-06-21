class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("O veículo está acelerando.")

    def frear(self):
        print("O veículo está freando.")
    
    def buzinar(self):
        print("PUUUUUUUUUUUUUUU")


class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def abrir_porta(self):
        print("Abrindo uma porta do carro.")
    
    def buzinar(self):
        print("POOOOOOOOOO")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        print("A moto está dando o Grau.")
        
    def buzinar(self):
        print("PIIIIIIIIIIIII")


# Criando instâncias das classes
veiculoA = Veiculo("VeiculoAA", "AA")

carro = Carro("Toyota", "Corolla", 4)
carro.acelerar()
carro.abrir_porta()

moto = Moto("Honda", "CBR600RR", 600)
moto.acelerar()
moto.empinar()

carro.buzinar()
moto.buzinar()

veiculoA.buzinar()