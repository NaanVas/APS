import csv
from modelo.livro import Livro

class LivroDAO:
    def __init__(self):
        self.arquivo_csv = 'livros.csv'

    def salvar_livro(self, livro):
        with open(self.arquivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Titulo', 'Autor', 'Editora', 'Ano de Publicacao', 'Emprestado'])
            writer.writerow([livro.get_titulo(), livro.get_autor(), livro.get_editora(), livro.get_ano_publicacao(), livro.is_emprestado()])
            
        print(f"Livro '{livro.get_titulo()}' salvo com sucesso no arquivo CSV.")

    def excluir_livro(self, titulo):
        livros = self.listar_livros()
        livros_filtrados = [livro for livro in livros if livro.get_titulo() != titulo]
        self._salvar_todos_livros(livros_filtrados)
        print(f"Livro '{titulo}' excluído com sucesso.")

    def buscar_livro(self, titulo):
        with open(self.arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Titulo'] == titulo:
                    livro = Livro(row['Titulo'], row['Autor'], row['Editora'], row['Ano de Publicacao'])
                    livro.set_emprestado(row['Emprestado'].lower() == 'true')
                    return livro
        return None

    def listar_livros(self):
        livros = []
        with open(self.arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                livro = Livro(row['Titulo'], row['Autor'], row['Editora'], row['Ano de Publicacao'])
                livro.set_emprestado(row['Emprestado'].lower() == 'true')
                livros.append(livro)
        return livros
    
    def _salvar_todos_livros(self, livros):
        with open(self.arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Titulo', 'Autor', 'Editora', 'Ano de Publicacao', 'Emprestado'])
            for livro in livros:
                writer.writerow([livro.get_titulo(), livro.get_autor(), livro.get_editora(), livro.get_ano_publicacao(), livro.is_emprestado()])