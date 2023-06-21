import math

while True:
    try:
        num = int(input("Digite um número inteiro: "))
        raiz = math.sqrt(num)
        print(f"\nRaiz quadrada de {num} = {raiz}\n")
        break
    except ValueError:
        print(f"\nErro: número inválido\n")
        print("Tente novamente")
    except Exception as e:
        print(f"\nErro: {str(e)}\n",)
        