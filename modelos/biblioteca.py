class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        #inicialmente desativada, utilizo underscore para indicar atributo privado
        self._ativo = False 
        Biblioteca.bibliotecas.append(self) #adiciona a biblioteca na lista de bibliotecas
    
    def __str__(self):
        return self.nome
    
    @classmethod #método de classe para listar todas as bibliotecas
    def listar_bibliotecas(cls): #cls refere-se à própria classe sem necessidade de instanciar um objeto
        print(f"{'Nome da Biblioteca'.ljust(25)} | {'Estado'}") #crio o cabeçalho da tabela
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | Ativo: {biblioteca.ativo}") #ljust alinha o texto à esquerda com 25 caracteres de largura
    
    #alterna o estado da biblioteca entre ativo e inativo
    #busca o atributo privado _ativo e inverte seu valor 
    #podemos chamar este método de SET
    def alterna_estado(self):        
        self._ativo = not self._ativo
    
    #property para acessar o estado da biblioteca, sem expor o atributo privado diretamente
    #neste caso, retorna "ativada" ou "desativada" baseado no valor booleano de _ativo
    #Aqui é feito o GET do atributo
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"
    
biblioteca_cidade = Biblioteca("Biblioteca da Cidade") 
#biblioteca_cidade._ativo = "True"
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")  

 
biblioteca_cidade.alterna_estado()  # Ativa a biblioteca
#print(biblioteca_cidade)  # Output: Biblioteca da Cidade
biblioteca_shopping.alterna_estado()  # Ativa a biblioteca
#print(biblioteca_shopping)  # Output: Biblioteca do Shopping

biblioteca_cidade.listar_bibliotecas()
