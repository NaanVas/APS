from persistencia.livro_dao import LivroDAO

class LivroView:
    def __init__(self):
        self.livro_dao = LivroDAO()

    def listar_e_imprimir_livros(self):
        livros = self.livro_dao.listar_livros()
        for livro in livros:
            self.imprimir_livro(livro)

    def imprimir_livro(self, livro):
        print(f"Titulo: {livro.get_titulo()}")
        print(f"Autor: {livro.get_autor()}")
        print(f"Editora: {livro.get_editora()}")
        print(f"Ano de Publicacao: {livro.get_ano_publicacao()}")
        print()

    def imprimir_livro_por_titulo(self, titulo):
            livro = self.livro_dao.buscar_livro(titulo)
            if livro:
                self.imprimir_livro(livro)
            else:
                print(f"Livro com titulo '{titulo}' nao encontrado.")