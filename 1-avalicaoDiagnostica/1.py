#Faça um programa que receba dois números e mostre qual deles é o maior.

num1 = int(input("Digite o 1 número: "))
num2 = int(input("Digite o 2 número: "))

if num1 > num2:
    print(num1, "é maior do que ", num2)
elif num1 < num2:
    print(num2, "é maior do que ", num1)
else:
    print(num1, "é igual a ", num2);