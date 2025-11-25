from modelos.biblioteca import Biblioteca

Biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
Biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

Biblioteca_cidade.alterna_estado()  # Ativa a biblioteca

Biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
Biblioteca_cidade.receber_avaliacao("Siclano", 9.5)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()

