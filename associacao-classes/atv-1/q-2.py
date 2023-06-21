"""
Implemente um algoritmo que modele a associação simples entre as classes Cliente, Pedido e Produto.
Cada cliente pode realizar vários pedidos, e cada pedido pode conter vários produtos. O algoritmo deve
permitir cadastrar um cliente, adicionar produtos a um pedido específico e exibir os detalhes do cliente,
seus pedidos e os produtos de cada pedido
"""

class Item:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
    
    def informacoes_item(self):
        print("Item: {} / valor: R$ {}".format(self.__nome, self.__preco))

class Pedido:
    def __init__(self, numero: int, data: str):
        self.__numero = numero
        self.__data = data
        self.__itens = []
        
    def adicionar_item(self, item: Item):
        self.__itens.append(item)
        
    def listar_item(self):
        for item in self.__itens:
            item.informacoes_item()
    
    def informacoes_pedido(self):
        print(f"Número: {self.__numero} / Data: {self.__data}")
            
            
class Cliente:
    def __init__(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email
        self.__pedidos = []
    
    def adicionar_pedido(self, pedido: Pedido):
        self.__pedidos.append(pedido)
        
    def listar_pedidos(self):
        for pedido in self.__pedidos:
            pedido.informacoes_pedido()
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @email.setter
    def email(self, email):
        self.__email = email
    
        
# Cadastrando um cliente
cliente1 = Cliente("João", "joao@example.com")

# Criando um pedido para o cliente
pedido1 = Pedido(1, "2023-05-17")

# Criando os produtos
produto1 = Item("Camiseta", 29.99)
produto2 = Item("Calça", 49.99)

# Adicionando produtos ao pedido
pedido1.adicionar_item(produto1)
pedido1.adicionar_item(produto2)

# Associando o pedido ao cliente
cliente1.adicionar_pedido(pedido1)

# Exibindo os detalhes do cliente, seus pedidos e os produtos de cada pedido
print("Detalhes do Cliente:")
print(f"Nome: {cliente1.nome}")
print(f"E-mail: {cliente1.email}")

print("\nPedidos do Cliente:")
cliente1.listar_pedidos()
print("\nProdutos do pedido:")
pedido1.listar_item()
