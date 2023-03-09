valorDia = 30

diasTrabalhados = int(input('Digite o nº de dias trabalhados: '))

salario = (valorDia * diasTrabalhados)

salarioComImposto = salario - (salario * 0.08)

print('Valor liquído R$', salarioComImposto)