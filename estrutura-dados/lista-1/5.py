#Faça um Programa que leia 20 números inteiros e armazene-os uma lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima as três listas.

lista = []

print('Digite 20 números inteiros:')
for i in range(20):
    num = int(input())
    lista.append(num)

pares = [n for n in lista if n % 2 == 0]
impares = [n for n in lista if n % 2 != 0]

print('Lista completa =', lista)
print('Números pares =', pares)
print('Números ímpares =', impares)