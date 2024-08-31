class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto):
        self.itens.append(produto)

    def remover_item(self, produto):
        self.itens.remove(produto)

    def exibir_carrinho(self):
        if len(self.itens) == 0:
            print("O carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            for produto in self.itens:
                print(f"- {produto.nome}: R${produto.preco}")


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = CarrinhoDeCompras()

    def adicionar_item_ao_carrinho(self, produto):
        self.carrinho.adicionar_item(produto)

    def remover_item_do_carrinho(self, produto):
        self.carrinho.remover_item(produto)

    def exibir_carrinho(self):
        self.carrinho.exibir_carrinho()


# Exemplo de uso:
# Criar alguns produtos
produto1 = Produto("Camiseta", 29.90)
produto2 = Produto("Calça", 59.90)
produto3 = Produto("Meias", 9.90)

# Criar uma pessoa
pessoa = Pessoa("João")

# Adicionar produtos ao carrinho da pessoa
pessoa.adicionar_item_ao_carrinho(produto1)
pessoa.adicionar_item_ao_carrinho(produto2)

# Exibir o carrinho da pessoa
pessoa.exibir_carrinho()

# Remover um item do carrinho da pessoa
pessoa.remover_item_do_carrinho(produto1)

# Exibir o carrinho novamente
pessoa.exibir_carrinho()
