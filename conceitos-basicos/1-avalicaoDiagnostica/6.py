#Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.

# n = int(input("Digite um numero inteiro par: "))

n = 10
contador = 0

if n %2 != 0:
    print("ERRO! O numero deve ser par")
else:
    while contador <= n:
        print(contador)
        contador += 2