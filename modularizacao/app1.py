

#OBS. dependendo da aplicação é mais recomendado especificar o que quer importar para não gastar processamento atoa
import basics_funciontions #importa TUDO da pasta basics_funciontions  e trata 'basics_funciontions' como uma classe
from basics_funciontions import * #importa tudo sem tratar como classe 

#utilizar como se fosse classe

#import basics_funciontions
print(basics_funciontions.soma(2, 4))
print(basics_funciontions.IDADE)

#from basics_funciontions import *
print(soma(2, 4))
print(IDADE)