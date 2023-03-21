#Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que compõem o número
while True:
    num = int(input('\nDigite um número entre 100 e 999: '))
    if 100 <= num <= 999:
        break
    print('Número inválido! Digite novamente')

# for i in range(3): #repete 3 vezes
#     algorismo = num % 10 
#     print('Algorismo', i + 1, ':', algorismo)
#     num = num // 10 #resultado INT


for i in range(0,3): #repete 3 vezes
    algorismo = num // (10 ** (2-i))  #5
    print('Algorismo', i + 1, ':', algorismo) #6
    num = num % (10 ** (2-i)) #6