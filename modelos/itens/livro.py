from modelos.itens.item_biblioteca import ItemBiblioteca

#Class especializada, uma vez que herda de ItemBiblioteca e ainda adiciona novos atributos
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco) # Chama o construtor da classe pai
        self.isbn = isbn