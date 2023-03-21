alturaDegrau = float(input('Digite a algura do degrau em cm: '))
alturaDestino = float(input('Digite a altura que deseja alçancar em m: '))

#converte m para cm
convercao = alturaDestino * 100

qdtDeEscadas = convercao / alturaDegrau

print('Para atingir', alturaDestino, 'm, você precisará subir', round(qdtDeEscadas, 2), 'escadas')