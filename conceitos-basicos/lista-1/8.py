segundosTotais = int(input('Digite um tempo em segundos: '))

hora = int(segundosTotais / 3600)
min = int(segundosTotais % 3600 / 60)
seg = int(segundosTotais % 3600 % 60)

print(segundosTotais,'s', '==', hora, 'h:', min, 'min:', seg,'s')