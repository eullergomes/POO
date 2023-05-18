class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b

operacoes = Calculadora()

a = 8
b = 90

print(f"Soma: {operacoes.somar(a, b)}")
print(f"Subtração: {operacoes.subtrair(a, b)}")
print(f"Multiplicação: {operacoes.multiplicar(a, b)}")
print(f"Divisão: {round(operacoes.dividir(a, b), 2)}")