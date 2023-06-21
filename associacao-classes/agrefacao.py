class Item:
    def __init__ (self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
    
    def mostrar_item(self):
        print(f'Nome: {self.__nome} / Preço: {self.__preco}')
        print()

class Carrinho:
    def __init__ (self):
        self.__itens = []
    
    def adicionar_item(self, item: Item):
        self.__itens.append(item)

    def remover_item(self, item: Item):
        if item in self.__itens:
            self.__itens.remove(item)
    def mostrar_itens(self):
        for item in self.__itens:
            item.mostrar_item()

itemA = Item('banana', '8')
itemB = Item('maça', '1.5')
itemC = Item('uva', '10')

meu_carrinho = Carrinho()
meu_carrinho.adicionar_item(itemA)
meu_carrinho.adicionar_item(itemB)
meu_carrinho.adicionar_item(itemC)

meu_carrinho.mostrar_itens()