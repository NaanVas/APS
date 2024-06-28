from modelo.livro import Livro
from modelo.autor import Autor
from persistencia.livro_dao import LivroDAO  
from persistencia.autor_dao import AutorDAO

class LivroController:
    def __init__(self):
        self.livro_dao = LivroDAO()
        self.autor_dao = AutorDAO()

    def cadastrar_livro(self, titulo, autor_nome, editora, ano_publicacao):
        livro_existente = self.livro_dao.buscar_livro(titulo)
        if livro_existente:
            return f"O livro '{livro_existente.get_titulo()} já está cadastrado"
        
        autor = self.autor_dao.buscar_autor(autor_nome)
        if not autor:
            novo_autor = Autor(autor_nome, '', '')
            novo_autor = self.autor_dao.salvar_autor(novo_autor)
            print(f"Autor '{autor_nome}' não encontrado. Autor cadastrado com nome.")
            autor = autor_nome

        livro = Livro(titulo, autor, editora, ano_publicacao)
        self.livro_dao.salvar_livro(livro)
        return None

    def excluir_livro(self, titulo):
        livro = self.livro_dao.buscar_livro(titulo)
        if livro:
            self.livro_dao.excluir_livro(titulo)
            return None
        else:
            return f"Livro '{titulo}' não encontrado."

    def buscar_livro(self, titulo):
        return self.livro_dao.buscar_livro(titulo)
    
    def listar_livros(self):
        return self.livro_dao.listar_livros()