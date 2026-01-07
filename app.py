from modelos.biblioteca import Biblioteca

"""
Comandos para inspecionar módulos em Python

import modelos.itens.item_biblioteca as mod
import inspect

print("ARQUIVO:", mod.__file__)
print("DIR:", dir(mod))
print("SOURCE:\n", inspect.getsource(mod))
"""
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

Biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
Biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.00, "084-3245")
livro2 = Livro("A Revolução dos Bichos", "George Orwell", 25.00, "084-3246")
revista1 = Revista("National Geographic", "John Doe", 15.00, "Quinta")

Biblioteca_cidade.adicionar_item(livro1)
Biblioteca_cidade.adicionar_item(livro2)
Biblioteca_cidade.adicionar_item(revista1)

#Biblioteca_cidade.alterna_estado()  # Ativa a biblioteca

#Biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
#Biblioteca_cidade.receber_avaliacao("Siclano", 9.5)
#Biblioteca_cidade.receber_avaliacao("Siclano", 6.5)

def main():
    #Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
    Biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()

