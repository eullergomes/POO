
lista1 = [1,2,3,4,5]
lista_vazia1 = []
lista_vazia2 = list()

print(lista1)
print(lista1[2])

frutas = ['maçã', 'banana', 'morango', 'kiwi']
lista_mista = ['hello', True, 3.14]
lista_alinhada = [[1,2,3], [4,5,6], [7,8,9]]

print(frutas)
print(frutas[0])
print(lista_alinhada[2])

#slicing
print(frutas[0:3]) #0-2

#acessando valores
for fruta in frutas:
    print(fruta)

#alterando valores
frutas[2] = 'mamão'
print(frutas)

#alterando dois valores
frutas[0:2] = ['melancia', 'morango'] #0-1
print(frutas)

#METODOS
frutas.append('açaí') #add no final da lista
frutas.insert(1, 'melancia') #add em uma pos. ESPECÍFICA 
print(frutas)

frutas.remove('mamão') #remove elem. específico
print(frutas)

numbers = [1,2,3,4,5]
new_numbers = [6,7,8]
numbers.extend(new_numbers) #add varios elem. na lista
print(numbers)

fruta_removida = frutas.pop() #remove o ultimo elemento e add em uma variavel
print(frutas)
print('Fruta removida:', fruta_removida)

numbers.remove(2) #remove pela posição
print(numbers)

del numbers[6] #tbm remove pela posição
print(numbers)

numbers.clear() #limpa a lista
print(numbers)


#LOOPS EM LISTAS
minha_lista = [1,2,3,4,5]
for item in minha_lista:
    print(item)

for indice, item in enumerate(minha_lista): #mostra o indice e o elemento
    print(indice, item)


