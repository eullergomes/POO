#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
medias = []

for i in range(10):
    notas = []
    print(f'Digite as notas do aluno {i}')
    for j in range(4):
        print(f'Nota {j}:')
        nota = float(input())
        notas.append(nota)
    alunos.append(notas)
    media = sum(notas) / len(notas)

    if media >= 7.0:
        medias.append(media)

print('\nTodos os alunos =',alunos)
print('Alunos aprovados =', len(medias))