#Faça um programa que receba um número inteiro e verifique se este número é par ou impar.

num = int(input('Digite um número inteiro: '))

if num %2 == 0:
    print(num, 'é par')
else:
    print(num, 'é ímpar')