class Contato:
    def __init__(self, email: str, telefone: str):
        self.email = email
        self.telefone = telefone
    
class Cliente:
    def __init__(self, nome: str, cnpj: str, contato=[]):
        self.nome = nome
        self.cnpj = cnpj
        self.__contato = contato
    
    def add_contato(self, email: str, telefone: str) -> None:
        novo_contato = Contato(email, telefone)
        self.__contato.append(novo_contato)

    def detalhes(self) -> None:
        print(f"{self.nome}, CNPJ: {self.cnpj}")
        print("Contatos:")
        for contato in self.__contato:
            print(f" E-mail: {contato.email}, Telefone: {contato.telefone}")

meu_cliente = Cliente("João Silva", "00.000.000/0001-00")
meu_cliente.add_contato("joao.silva@hotmail.com", "+55 11 1234-5678")
meu_cliente.add_contato("joao.silva@gmail.com", "+55 11 9876-5432")
meu_cliente.detalhes()

#Mostre qndo deletar
del meu_cliente
