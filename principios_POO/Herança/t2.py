class Mae:
    def __init__(self, nome, endereco):
        self.endereco = endereco
        self.nome = nome
        
    def comer(self):
        print("Eu estou comendo!!!")
        
    def estudar(self, disciplina):
        print(f"Eu estou estudando {disciplina}")
        
class Filha (Mae):
    def __init__(self, nome, endereco, idade: int):
        #referência para essa classe, herda os atributos do __init__ de Mae
        super().__init__(nome, endereco)
        self.__idade = idade
        
    @property
    def idade(self):
        return self.__idade
        
    def brincar(self, brinquedo):
        print(f"Estou brincando com {brinquedo}")
        

        
mae = Mae('Maria', 'Rua Um')
clara = Filha('Clara', 'SP', 7)
clara.estudar('Matemática')
print(clara._Filha__idade)
print(clara.idade)

print(f"Nome: {mae.nome} / Endereço: {mae.endereco}")
print(f"\nNome: {clara.nome} / Endereço: {clara.endereco}")
clara.brincar('boneca')

