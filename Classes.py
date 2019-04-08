class Autor():

  def __init__(self, nome, nascimento):
    self.nome = nome
    self.primeiro = nome.split()[0].title()
    self.meio = " ".join(nome.split()[1:-1]).title()
    self.ultimo = nome.split()[-1].lower().title()
    self.nascimento = nascimento

  @property
  def nome_como_citado(self):
    return "{last_name} {first_name_letter}.".format(last_name=self.nome.split()[-1].upper(), first_name_letter=self.nome.split()[0][0].upper())

class Livro():
  def __init__(self, titulo, ano, autor):
    self.autor = autor
    self.ano = ano
    self.titulo = titulo

  @property
  def referencia_livro(self):
    return "{tirulo}, {ano}, {autor}".format(autor=self.autor, tirulo=self.titulo, ano=self.ano)

  def __str__(self):
    return self.referencia_livro

class Biblioteca():

  def __init__(self, livro):
    self.livros = livro

  def add_livro(self, livro):
    self.livros.append(livro)

  def __str__(self):
    return "; ".join([str(livro) for livro in self.livros])