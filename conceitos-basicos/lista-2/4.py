#Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina. -.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1 < 0.0 or n1 >= 10.0) and (n2 < 0.0 or n2 >= 10.0):
    print('As duas notas são inválidas')
elif n1 < 0.0 or n1 >= 10.0:
    print('A primeira nota é inválida')
elif n2 < 0.0 or n2 >= 10.0:
    print('A segunda nota é inválida')
else:
    print('Notas válidas')
    media = (n1 + n2) / 2
    print('Média =', media)