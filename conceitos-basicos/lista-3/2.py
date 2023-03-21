#Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.

n = int(input('Digite um número inteiro positivo PAR: '))

if n %2 != 0:
    print('O número não é par!')
else:
    cont = 0
    while cont <= n:
        if cont %2 == 0:
            print(cont)
        cont += 1 