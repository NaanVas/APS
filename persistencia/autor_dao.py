from modelo.autor import Autor
from persistencia.dao_base import DAOBase

class AutorDAO(DAOBase):
    def __init__(self, arquivo_csv_autores='autores.csv'):
        super().__init__(arquivo_csv_autores)

    def salvar_autor(self, autor):
        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, ['Nome', 'Nacionalidade', 'Data de Nascimento'])
            self._escrever_linha(file, [autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento()])

    def excluir_autor(self, nome):
        autores = self.listar_autores()
        autores_filtrados = [autor for autor in autores if autor.get_nome() != nome]
        self._salvar_todos_autores(autores_filtrados)

    def buscar_autor(self, nome):
        for row in self._ler_arquivo():
            if row['Nome'] == nome:
                return Autor(row['Nome'], row['Nacionalidade'], row['Data de Nascimento'])
        return None

    def listar_autores(self):
        autores = []
        for row in self._ler_arquivo():
            autor = Autor(row['Nome'], row['Nacionalidade'], row['Data de Nascimento'])
            autores.append(autor)
        return autores

    def _salvar_todos_autores(self, autores):
        cabecalho = ['Nome', 'Nacionalidade', 'Data de Nascimento']
        dados = [[autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento()] for autor in autores]
        self._salvar_todos(cabecalho, dados)
