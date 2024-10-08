from persistencia.dao_base import DAOBase
from modelo.livro import Livro

class LivroDAO(DAOBase):
    def __init__(self):
        super().__init__('livros.csv')

    def salvar_livro(self, livro):
        cabecalho = ['Titulo', 'Autor', 'Editora', 'Ano de Publicacao', 'Emprestado']
        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, cabecalho)
            self._escrever_linha(file, [
                livro.get_titulo(), 
                livro.get_autor(), 
                livro.get_editora(), 
                livro.get_ano_publicacao(), 
                livro.is_emprestado()
            ])

    def excluir_livro(self, titulo):
        livros = self.listar_livros()
        livros_filtrados = [livro for livro in livros if livro.get_titulo() != titulo]
        self._salvar_todos_livros(livros_filtrados)

    def buscar_livro(self, titulo):
        livros = self._ler_arquivo()
        for row in livros:
            if row['Titulo'] == titulo:
                livro = Livro(row['Titulo'], row['Autor'], row['Editora'], row['Ano de Publicacao'])
                livro.set_emprestado(row['Emprestado'].lower() == 'true')
                return livro
        return None

    def listar_livros(self):
        livros = []
        for row in self._ler_arquivo():
            livro = Livro(row['Titulo'], row['Autor'], row['Editora'], row['Ano de Publicacao'])
            livro.set_emprestado(row['Emprestado'].lower() == 'true')
            livros.append(livro)
        return livros
    
    def _salvar_todos_livros(self, livros):
        cabecalho = ['Titulo', 'Autor', 'Editora', 'Ano de Publicacao', 'Emprestado']
        dados = [
            [livro.get_titulo(), livro.get_autor(), livro.get_editora(), livro.get_ano_publicacao(), livro.is_emprestado()]
            for livro in livros
        ]
        self._salvar_todos(cabecalho, dados)
