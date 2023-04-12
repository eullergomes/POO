#f sem retorno
def imprimir():
    print('Executando...')

imprimir()

#f com retorno
def soma(a, b):
    return a + b

print('Soma =', soma(5, 6))

#recebe vários parâmetros
def funcao (*args):
    return args #retorna em uma tupla

print('Valores inseridos:', funcao('joao', 'otavio', 'euller','mateus'))


#parametros são dicionários, ou seja, retorna um dicionário
def minha_func (**kwargs):
    return kwargs

meu_dic = minha_func(nome='euller', nota1=8, nota2 = 9)
print(meu_dic)
