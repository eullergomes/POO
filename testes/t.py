array = ['euller', 'joao', 'maria']
nome = 'joao'

for i in array:
    print(f'{i}')

for i in array:
    if nome == i:
        del i

print('\ndepois:\n')
for i in array:
    print(f'{i}')