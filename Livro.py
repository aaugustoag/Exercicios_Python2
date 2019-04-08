from Classes import Autor

class ref_livro:
    def __init__(self, titulo, ano, autor):
        self.autor = autor
        self.ano = ano
        self.titulo = titulo

    @property
    def referencia_livro(self):
        return "{tirulo}, {ano}, {autor}".format(autor=self.autor, tirulo=self.titulo, ano=self.ano)
