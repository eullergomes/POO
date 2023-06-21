try:
    num = int(input("Digite um número inteiro: ")) #TypeError
    print(f"Número digitado: {num}")

    num2 = int(input("Digite um numero dividir por 10: ")) #ZeroDivisionError
    resultado = 10 / num2

    lista = [10, 20, 30]
    indice = int(input("Digite um índice da lista a ser acessado: ")) #TypeError ou IndexError
    print(f"Índice: {indice} / Valor: {lista[indice]}")

except (TypeError, IndexError):
    print("Erro! Tipo de número ou indice invalido")
except ZeroDivisionError:
    print("Erro! Divisão por 0")
    
#evitar usar pois não é uma excessão específica
except Exception as e: #armazena o erro na variável 'e'
    print(f"Erro desconhecido", str(e))

