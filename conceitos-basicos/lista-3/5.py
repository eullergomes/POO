#Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.

while True:
    n = int(input("Digite o número de Fibonacci: "))
    if n > 0:
        break
    print('Número inválido! Tente novamente')

ant = 0
prox = 0

while prox < n:
    print(prox)
    prox = prox + ant
    ant = prox - ant
    if prox == 0:
        prox = prox + 1