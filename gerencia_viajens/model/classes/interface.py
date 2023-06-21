from abc import ABC, abstractmethod 

class ManagerInterface(ABC):
    @abstractmethod
    def cadastrar(self) -> None:
        pass
    
    @abstractmethod
    def remover(self) -> None:
        pass
    
    @abstractmethod
    def editar(self) -> None:
        pass
    
    @abstractmethod
    def pesquisar(self) -> None:
        pass
    

# class ServicesInterface(ABC):
#     @abstractmethod
#     def registar(self) -> None:
#         pass