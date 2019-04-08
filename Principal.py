from Classes import Autor
from Classes import Livro
from Classes import Biblioteca

nome1 = "Alexandre Augusto Aguiar Gomes"
nome2 = "daniel hassan dalip"
nome3 = "maluco da internet"

titulo1 = "Aula Python"
lista_autores1 = []
ano1 = 2019

titulo2 = "Baby Shark"
lista_autores2 = []
ano2 = 2018

lista_livros = []


print("\nAutores:")
lista_autores1.append(nome1.split()[-1].upper()+" "+nome1.split()[0][0].upper()+".")
print(lista_autores1)
lista_autores1.append(nome2.split()[-1].upper()+" "+nome2.split()[0][0].upper()+".")
print(lista_autores1)
print("\nLivros")
lista_livros.append([titulo1, lista_autores1, ano1])
print(lista_livros)
lista_autores2.append(nome3.split()[-1].upper()+" "+nome3.split()[0][0].upper()+".")
lista_livros.append([titulo2, lista_autores2, ano2])
print(lista_livros)

print("\nTarefa Autor")
a1 = Autor.autor_name(nome1,"01/05/1979")
print(a1.nome)
print(a1.nome_como_citado)
print(a1.primeiro)
print(a1.meio)
print(a1.ultimo)
print(a1.nascimento)

print("\nTarefa Livro")
l1 = Livro.ref_livro(titulo1, ano1, a1.nome_como_citado)
print(l1.referencia_livro)

print("\nTarefa Biblioteca")
b1 = Biblioteca.livros.adiciona_livro(l1.referencia_livro)
print(b1)
