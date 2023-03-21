#Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

n = int(input('Digite um número inteiro: '))
cont = 0
impar = 1

while (cont < n): #qtd de numeros impares
    if impar % 2 != 0: #numeros impares
        print(impar)
        cont += 1
    impar += 1