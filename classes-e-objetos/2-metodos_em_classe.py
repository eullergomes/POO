class Aluno():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def aniversario(self):
        self.idade += 1
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos")
        
pessoa1 = Aluno('Euller', 19)
pessoa1.apresentar()

pessoa1.aniversario()
pessoa1.apresentar()