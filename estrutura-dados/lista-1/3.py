#Faça um Programa que leia 4 notas, adicione em uma lista e mostre as notas e a média na tela.

notas = []

print('Digite as notas:');

for i in range(4):
    print(f'Nota {i}:')
    num = float(input())
    notas.append(num)

print('Notas =', notas)

media = sum(notas) / len(notas)
print('Média', media)

#sum() --- soma dos itens da lista
#map() --- aplica funcao a cada item da lista