#Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

cont = int(input('Digite quantos números serão lidos: '))
vezesRepetidas = 1

print('Digite os', cont, 'números:')
num1 = int(input())

maior = num1
# menor = num1

cont -= 1 
for i in range(cont): 
    num = int(input())

    if num > maior:
        maior = num
        vezesRepetidas = 0
    if num == maior:
        vezesRepetidas += 1
    # if num < menor:
    #     menor = num
        

print('Maior número:', maior)
# print('Menor número:', menor)
print('Vezes repetidas:', vezesRepetidas)
