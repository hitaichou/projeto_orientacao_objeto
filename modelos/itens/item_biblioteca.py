from abc import ABC, abstractmethod #método abstrato

#todas as classes que instanciar, precisa implementar o método aplicar_desconto

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, preco): #classe com construtor
        self._titulo = titulo
        self._autor = autor
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self): #método para aplicar desconto
        pass