class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome(self): #apenas read de arquivos priv
        return self.__nome

    @nome.setter #apenas write de arquivos priv
    def nome(self, nome):
        self.__nome = nome

        
pessoa1 = Pessoa('euller', 19)
pessoa1.nome = 'João'
print(f"Nome: {pessoa1.nome}")