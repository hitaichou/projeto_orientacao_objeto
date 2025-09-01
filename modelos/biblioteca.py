class Biblioteca:
    nome = ""
    ativo = False

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Biblioteca da cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()

# Lista de objetos da classe Biblioteca
bibliotecas = [biblioteca_cidade, biblioteca_shopping] 

# A função vars() em Python retorna o __dict__ (dicionário de atributos) de um objeto, 
# que contém todos os atributos do objeto e seus valores correspondentes.
# No caso do exemplo fornecido, vars(biblioteca_cidade) retornará um dicionário 
# com os atributos 'nome' e 'ativo' do objeto biblioteca_cidade.
print(vars(biblioteca_cidade))  

print(vars(biblioteca_shopping)) # Retorna um dicionário vazio, pois nenhum atributo foi definido para este objeto.

# Exibindo os atributos de todos os objetos na lista bibliotecas
for biblioteca in bibliotecas:
    print(vars(biblioteca))
