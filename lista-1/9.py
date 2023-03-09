#Início
horaInicio = int(input('Digite a hora de início: '))
minInicio = int(input('Digite os minutos de início: '))
segInicio = int(input('Digite os segundos de início: '))

#Duração
duracao = int(input('Digite a duração do experimento em segundos: '))

segundosTotais =(horaInicio * 3600) + (minInicio * 60) + segInicio + duracao

horaDuracao = int(duracao / 3600)
minDuracao = int(duracao % 3600 / 60)
segDuracao = int(duracao % 3600 % 60)

#Fim
horaFim = int(segundosTotais / 3600)
minFim = int(segundosTotais % 3600 / 60)
segFim = int(segundosTotais % 3600 % 60)

print('\nHorário de início:', horaInicio,'h:', minInicio,'min:', segInicio,'s')

print('Tempo de duração:', horaDuracao,'h:', minDuracao,'min:', segDuracao,'s')

print('Horário de terminio:', horaFim,'h:', minFim,'min:', segFim,'s\n')

#poderia criar funções pra diminuir o código