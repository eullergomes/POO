class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

class Distribuidor:
    def __init__(self, codigo: int, nome: str, endereco: float):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
            
        
class ProdutoFisico(Produto):
    def __init__(self, codigo: int, nome: str, preco: float, peso: float):
        super().__init__(codigo, nome, preco)
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.peso = peso
        
class ProdutoVirtual(Produto):
    def __init__(self, codigo: int, nome: str, preco: float, tamanho_arquivo: float):
        super().__init__(codigo, nome, preco)
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.tamanho_arquivo = tamanho_arquivo