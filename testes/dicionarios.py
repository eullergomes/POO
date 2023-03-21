pessoa = {
    'nome': 'Euller',
    'idade': 19,
    'curso': 'BCC',
    'adress': {
        'street': 'Rua Um',
        'number': 10
    }
}

rua = pessoa['adress']['street'] #acesando com chave []
print(rua)

nome = pessoa.get('nome') #acessando com get
print(nome)


print(pessoa)

#alterando dados
pessoa['idade'] = 20
print(pessoa)

#adicionando mais valores
pessoa['peso'] = 65.6
print(pessoa)

#removendo valor
del pessoa['peso']
print(pessoa)

#atualizando VARIOS valores
pessoa.update({'nome': 21, 'curso': 'ADM', 'peso': 72})
print(pessoa)



dicionario = {'a': 1, 'b': 2, 'c': 3}
print(dicionario)

chaves = dicionario.keys() #retorna uma lista com as chaves
print(chaves)

valores = dicionario.values() #retorna uma lista com os valores
print(valores)

itens = dicionario.items() #retorna uma lista com tuplas contendo as chaves e valores
print(itens)

for i, v in dicionario.items():
    print(f'O {i} é {v}')

filme1 = {
    'nome': 'Star Wars',
    'ano': 1977,
    'autor': 'sei la'
    }

filme2 = {
    'nome': 'Homem Aranha',
    'ano': 1988,
    'autor': 'Stan le'
    }

locadora = []
locadora.append(filme1)
locadora.append(filme2)
print(locadora[0]['nome'])



