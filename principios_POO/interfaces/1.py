from abc import ABC, abstractmethod 
from typing import Type

class FormasInterface(ABC):
    @abstractmethod
    def get_perimetro(self) -> int:
        pass
    
    @abstractmethod
    def get_area(self) -> int:
        pass

class TerrenoQuadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado
    
    def get_perimetro(self) -> int:
        perimetro = self.lado * 4
        return perimetro

    def get_area(self) -> int:
        area = self.lado * self.lado
        return area

class TerrenoRetangulo(FormasInterface):
    def __init__(self, largura: int, comprimento: int) -> None:
        self.largura = largura
        self.comprimento = comprimento
    
    def get_perimetro(self) -> int:
        perimetro = (self.comprimento * 2) + (self.largura * 2)
        return perimetro

    def get_area(self) -> int:
        area = self.largura * self.comprimento
        return area
    
class Engenheiro:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    """
    Type[FormasInterface] -> específicando que poderá ser qualquer classe filha da classe FormasInterface
    """
    def medir_perimetro(self, terreno: Type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print("{} mediu o perímetro: {} m".format(self.nome, perimetro))
    
    def medir_area(self, terreno: Type[FormasInterface]):
        area = terreno.get_area()
        print("{} mediu a área: {} m".format(self.nome, area))
        
        
terrenoQ = TerrenoQuadrado(10)
terrenoR = TerrenoRetangulo(2, 3)

roger = Engenheiro('Roger')

roger.medir_area(terrenoQ)
roger.medir_area(terrenoR)

roger.medir_perimetro(terrenoQ)
roger.medir_perimetro(terrenoR)