#Faça um Programa que receba uma lista de 5 números inteiros e mostre-os.

lista = []

print('Digite 5 números inteiros:');

for i in range(5):
    num = int(input())
    lista.append(num)

print(lista)