class PessoaA:
    def se_apresentar(self):
        print("Olá, sou a pessoa A")
        
class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()
    
    #alterando o método herdado (altera apenas para essa classe)  
    def se_apresentar(self):
        print("Estou alterando esse método")
        
pessoaA = PessoaA()
pessoaB = PessoaB()

pessoaA.se_apresentar()
pessoaB.se_apresentar()