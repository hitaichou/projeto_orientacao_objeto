class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self.ativo = "False"        
        Biblioteca.bibliotecas.append(self) #adiciona a biblioteca na lista de bibliotecas
    
    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | Ativo: {biblioteca.ativo}")
    
biblioteca_cidade = Biblioteca("Biblioteca da Cidade") 
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")  

 
print(biblioteca_cidade)  # Output: Biblioteca da Cidade
print(biblioteca_shopping)  # Output: Biblioteca do Shopping

Biblioteca.listar_bibliotecas()
