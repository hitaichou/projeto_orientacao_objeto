from modelos.itens.item_biblioteca import ItemBiblioteca
# Classe especializada que herda de ItemBiblioteca e adiciona novos atributos
class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)  # Chama o construtor da classe pai
        self.edicao = edicao
        
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)  # Aplica um desconto de 5% de desconto