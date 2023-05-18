def check(dados, cod):
    for chave in dados:
        if cod == chave:
            return dados[chave]
    return


class ArmazenarDados():
    def __init__(self):  # retorna um dicionario vazio
        self.dados = {}

    def add_dados(self, cod: int, nome: str):
        pessoa = {'nome': nome, 'cod': cod}
        self.dados[cod] = pessoa

    def ver_dados(self): # ver todas as pessoas
        for pessoa in self.dados.values():
            print(f"Nome: {pessoa['nome']}, Cod: {pessoa['cod']}")
    
    def del_dados(self, cod: int):
        if cod in self.dados:
            del self.dados[cod]
        else:
            print("Pessoa não encontrada!")
            
    # def del_dados(self, cod:int):
    #     pessoa = check(self.dados, cod)
    #     if pessoa:
    #         del pessoa
    #     else:
    #         print("Pessoa não encontrada!")


pessoas = ArmazenarDados()
pessoas.add_dados(123, 'Euller')
pessoas.add_dados(456, 'João')
pessoas.add_dados(456, 'Jonatas')
pessoas.add_dados(789, 'Maria')
pessoas.ver_dados()
pessoas.del_dados(5)
print()

pessoas.ver_dados()
      

