valorTotal = float(input('Digite o valor total do produto R$: '))

totalPagar = valorTotal - (valorTotal * 0.1) #desconto 10%
parcelas = valorTotal / 3
comissaoAvista = totalPagar * 0.05
comissaoParcelado = valorTotal * 0.05

print('Valor do produto: R$', round(valorTotal, 2))
print('Valor com desconto: R$', round(totalPagar, 2))
print('Parcelas de 3x sem juros: R$', round(parcelas, 2))
print('Venda a vista - comissão do vendedor: R$', round(comissaoAvista, 2))
print('Venda a parcelada - comissão do vendedor: R$', round(comissaoParcelado, 2))

