class autor_name:

  def __init__(self, nome, nascimento):
    self.nome = nome
    self.primeiro =nome.split()[0]
    self.meio = nome.split()[1:-1]
    self.ultimo = nome.split()[-1]
    self.nascimento = nascimento

  @property
  def nome_como_citado(self):
    return "{last_name} {first_name_letter}.".format(last_name=self.nome.split()[-1].upper(), first_name_letter=self.nome.split()[0][0].upper())
