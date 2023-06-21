"""
Para utilizar o sistema, podemos realizar as seguintes ações:
    1. Cadastrar um novo autor.
    2. Cadastrar um novo livro, informando o título, ano e autor.
    3. Adicionar exemplares a um livro existente.
    4. Realizar um empréstimo, informando o usuário, data e exemplar a ser emprestado.
    5. Finalizar um empréstimo, marcando o exemplar como devolvido.
    6. O sistema deve permitir exibir os detalhes dos livros, autores, exemplares e empréstimos realizados.
"""

"""
    Se o exemplar está disponível, então FALSE
    Se o exemplar está indisponível, então TRUE
"""

class Exemplar:
    def __init__(self, numero: int, status: False):
        self.__numero = numero
        self.__status = status
    
    def informacoes_exemplar(self):
        print(f"Número: {self.__numero}\nStatus: {self.__status}")
        print()
        
    def disponivel(self):
        if self.__status == True:
            print("\nExemplar disponível!")
        else:
            print("\nExemplar indisponível!\n")
        
    def mudar_status(self):
        self.__status == True
        print(f"Exemplar: {self.__numero} alterada para {self.__status}\n")

class Autor:
    def __init__(self, nome: str, pais: str):
        self.__nome = nome
        self.__pais = pais
        
    def informacoes_autor(self):
        print(f"Autor: {self.__nome}\nPaís: {self.__pais}")
        print()
        
class Livro:
    def __init__(self, titulo: str, ano: int, autor: Autor):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__exemplares = []
    
    def informacoes_livro(self):
        print("INFORMAÇÕES DO LIVRO:")
        print(f"Título: {self.__titulo}")
        print(f"Ano: {self.__ano}")                         
        self.__autor.informacoes_autor()
        print()
    
    def adicionar_exemplar(self, exemplar: Exemplar):
        self.__exemplares.append(exemplar)
        
class Emprestimo:
    def __init__(self, usuario: str, data_emprestimo: str):
        self.__usuario = usuario
        self.__data_emprestimo = data_emprestimo
        self.__exemplares = []
        
    def adicionar_exemplar(self, exemplar: Exemplar):
        self.__exemplares.append(exemplar)
            
    def finalizar(self):
        for exemplar in self.__exemplares:
            exemplar.mudar_status()
            
    def emprestimos_realizados(self):
        for exemplar in self.__exemplares:
            exemplar.informacoes_exemplar()
            
    def info_emprestimo(self):
        print(f"Usuário: {self.__usuario}")
        print(f"Data: {self.__data_emprestimo}")
        print(f"Empréstimos realizados:")
        
        self.emprestimos_realizados()

#Cadastrar um novo autor     
autor1 = Autor('Euller', 'Brasil')
autor1.informacoes_autor()

#Cadastrar um novo livro, informando o título, ano e autor
livro1 = Livro('Meu 1º livro', 2023, autor1)
livro1.informacoes_livro()

#Adicionar exemplares a um livro existente
exemplar1 = Exemplar(1, True)
exemplar2 = Exemplar(2, False)
print("EXEMPLARES:\n")
exemplar1.informacoes_exemplar()
exemplar2.informacoes_exemplar()
livro1.adicionar_exemplar(exemplar1)
livro1.adicionar_exemplar(exemplar2)

#Realizar um empréstimo, informando o usuário, data e exemplar a ser emprestado
emprestimo1 = Emprestimo('João', '18/12/2003')
emprestimo1.adicionar_exemplar(exemplar1)

#Finalizar um empréstimo, marcando o exemplar como devolvido
emprestimo1.finalizar()

#O sistema deve permitir exibir os detalhes dos livros, autores, exemplares e empréstimos realizados
print("INFORMAÇÕES DO EMPRÉSTIMO:")
emprestimo1.info_emprestimo()

del livro1
print("Com livro deletado:\n")
exemplar1.informacoes_exemplar()