#Faça um Programa que receba uma lista de 10 números reais e mostre-os na ordem inversa.

lista = []

print('Digite 10 números reais:');

for i in range(10):
    num = float(input())
    lista.append(num)

print('Antes:')
print(lista)

print('\nDepois:')
lista.reverse()
print(lista)