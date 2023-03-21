#Faça um programa que receba um número inteiro e verifique se este número é par ou impar.

num = int(input("Digite um numero: "))

if num %2 == 0:
    print(num, "e par");
else:
    print(num, "e impar")