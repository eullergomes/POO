#raise permite que você crie suas próprias exceções ou levante exceções predefinidas para sinalizar 
# um erro ou condição especial durante a execução do programa. 

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitido.")
    if isinstance(b, str):
        raise TypeError("Divisão por string não é permitido")
    else:
        return a / b
try:
    resultado = dividir(10,'a')
    print("Resultado:", resultado)
except ValueError as e:
    print("Erro:", str(e))
except TypeError as e:
    print("Erro:", str(e))
except Exception as e:
    print("Erro desconhecido: ", str(e))