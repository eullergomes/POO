#Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais. .

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(num1, 'é maior do que', num2)
elif num1 == num2:
    print('Números iguais')
else:
    print(num2, 'é maior do que', num1)