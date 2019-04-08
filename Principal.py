from Classes import Classes

nome2 = "ALEXANDRE AUGUSTO AGUIAR GOMES"
nome1 = "daniel hassan dalip"
nome3 = "maluco da internet"

titulo1 = "Aula Python"
ano1 = 2019

titulo2 = "Baby Shark"
ano2 = 2018

titulo3 = "Arvore da Montanha"
ano3 = 2000

print("\nTarefa Autor")
a1 = Classes.Autor(nome1, "01/05/1979")
print(a1.nome)
print(a1.primeiro+" "+a1.meio+" "+a1.ultimo)
print(a1.nome_como_citado)
print(a1.nascimento)
a2 = Classes.Autor(nome2, "24/12/2017")
print(a2.nome)
print(a2.primeiro+" "+a2.meio+" "+a2.ultimo)
print(a2.nome_como_citado)
print(a2.nascimento)
a3 = Classes.Autor(nome3, "00/00/2000")
print(a3.nome_como_citado)

print("\nTarefa Livro")
l1 = Classes.Livro(titulo1, ano1, a1.nome_como_citado)
print(l1.referencia_livro)
l2 = Classes.Livro(titulo2, ano2, a2.nome_como_citado)
print(l2.referencia_livro)
l3 = Classes.Livro(titulo3, ano3, a3.nome_como_citado)
print(l3.referencia_livro)

print("\nTarefa Biblioteca")
b1 = Classes.Biblioteca([l1,l2])
print(b1)
b1.add_livro(l3)
print(b1)