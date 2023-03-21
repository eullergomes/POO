#Faça um Programa que leia lista  de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = ['a', 'b', 't', 'z', 'r', 'i', 'q', 'u']
vogais = ['a', 'e', 'i', 'o', 'u']

# print('Digite 10 caracteres para a lista')
# for i in range(10):
#     c = input()
#     lista.append(c[0])

consoantes = [letra for letra in lista if letra not in vogais]
qtd = len(consoantes)
 
print('Consoantes =', consoantes)
print('Quantidade =', qtd)