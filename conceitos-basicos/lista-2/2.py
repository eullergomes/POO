#Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(num1, 'é maior do que', num2)
elif num1 == num2:
    print(num1, 'é igual a', num2)
else:
    print(num2, 'é maior do que', num1)