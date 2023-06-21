def dividir(a, b):
    try:
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        else:
            return a / b
    except ValueError as e:
        print("Erro:", str(e))

a = 'a'

try:
    resultado = dividir(10, a)
    print("Resultado:", resultado)
except TypeError as e:
    print("Erro:", str(e))
