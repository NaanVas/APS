from modelo.autor import Autor

class Livro:
    def __init__(self, titulo, autor, editora, ano_publicacao):
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_editora(editora)
        self.set_ano_publicacao(ano_publicacao)
        self.emprestado = False

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def get_autor(self):
        return self._autor.get_nome() if isinstance(self._autor, Autor) else self._autor

    def set_autor(self, novo_autor):
        self._autor = novo_autor

    def get_editora(self):
        return self._editora

    def set_editora(self, nova_editora):
        self._editora = nova_editora

    def get_ano_publicacao(self):
        return self._ano_publicacao

    def set_ano_publicacao(self, novo_ano):
        self._ano_publicacao = novo_ano

    def is_emprestado(self):
        return self.emprestado

    def set_emprestado(self, emprestado):
        self.emprestado = emprestado
