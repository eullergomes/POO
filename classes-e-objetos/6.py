"""
Escreva uma classe chamada ContaBancaria que tenha os atributos saldo e titular e os métodos depositar, sacar e consultar_saldo. O método depositar deve receber um valor como parâmetro e adicioná-lo ao saldo. O método sacar deve receber um valor como parâmetro e subtraí-lo do saldo. O método consultar_saldo deve retornar o saldo atual da conta.
"""

class ContaBancaria:
    def __init__(self, titular: str, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        self.saldo -= valor

    def consultar_saldo(self):
        print(f"{self.titular}, seu saldo é de R$ {self.saldo}")
        
euller = ContaBancaria('Euller', 1000)
euller.depositar(90)
euller.sacar(290)
euller.consultar_saldo()