import math

#Execute para testar
try:
    resultado = 1/0
    print("Resultado:", resultado)
except:
    print("Erro: Divisão por zero não é permitida.")
  
# print(f"Erro em uma situação normal {1 / 0}") #ZeroDivisionError - divisão por 0
# print(f"Erro em uma situação normal {1 / 'b'}") #TypeError - tipo de dado inválido

# raiz = math.sqrt(-16) #ValueError - valor inválido
# print(raiz)

lista = [10, 20, 30]
print(lista[4]) #IndexError - indice de uma list/dict que não existe