import csv
from modelo.autor import Autor

class AutorDAO:
    def __init__(self):
        self.arquivo_csv_autores = 'autores.csv'

    def salvar_autor(self, autor):
        with open(self.arquivo_csv_autores, mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Nome', 'Nacionalidade', 'Data de Nascimento'])
            writer.writerow([autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento()])

        print(f'Autor {autor.get_nome()} salvo com sucesso no arquivo CSV.')

    def excluir_autor(self, nome):
        autores = self.listar_autores()
        autores_filtrados = [autor for autor in autores if autor.get_nome() != nome]
        self.salvar_todos_autores(autores_filtrados)
        print(f"Autor '{nome}' excluido com sucesso.")

    def buscar_autor(self, nome):
        with open(self.arquivo_csv_autores, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Nome'] == nome:
                    return Autor(row['Nome'], row['Nacionalidade'], row['Data de Nascimento'])
        return None

    def listar_autores(self):
        autores = []
        with open(self.arquivo_csv_autores, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                autor = Autor(row['Nome'], row['Nacionalidade'], row['Data de Nascimento'])
                autores.append(autor)
        return autores

    def salvar_todos_autores(self, autores):
        with open(self.arquivo_csv_autores, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Nacionalidade', 'Data de Nascimento'])
            for autor in autores:
                writer.writerow([autor.get_nome(), autor.get_nacionalidade(), autor.get_data_nascimento()])