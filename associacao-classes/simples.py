class Produto:
    def __init__(self, prod_nome: str, prod_valor: int):
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor
    
    def informacoes_prod(self):
        print("Produto: {} / valor: R$ {},00".format(self.__prod_nome, self.__prod_valor))
        
        
class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
        
    def add_produto(self, produto: Produto):
        self.__produtos.append(produto)
        
    def finalizar_compra(self):
        print("Compras Finalizadas!")

        for produto in self.__produtos:
              produto.informacoes_prod()
              
carrinho = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
mouse = Produto('Mouse', 50)

carrinho.add_produto(monitor)
carrinho.add_produto(mouse)
carrinho.finalizar_compra()