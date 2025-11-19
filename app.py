from modelos.biblioteca import Biblioteca

Biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
Biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

Biblioteca_cidade.alterna_estado()  # Ativa a biblioteca

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()

