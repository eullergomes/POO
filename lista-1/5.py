salarioBase = float(input('Digite o salário-base do funcionário R$: '))
imposto = salarioBase * 0.07
graficacao = salarioBase * 0.05

salarioTotal = salarioBase + graficacao - imposto

print('Salário a receber R$', salarioTotal)