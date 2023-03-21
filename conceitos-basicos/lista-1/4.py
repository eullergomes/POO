horaTrabalho = float(input('Digite o valor da hora de trabalho R$: '))
horaMes = int(input('Digite o nº de horas trabalhados no mês: '))

salario = horaTrabalho * horaMes
salarioTotal = salario + (salario * 0.1)

print('O encanador ganhará: R$', salarioTotal)