class Avaliacao:
    #o que é o atributo self? 
    #self é uma referência à instância atual da classe. Ele é usado para acessar variáveis que pertencem à classe.
    #A classe é privado, pois tem o uso do underline antes do nome do atributo, como em _atributo.
    def __init__(self, cliente, nota): 
        self._cliente = cliente
        self._nota = nota