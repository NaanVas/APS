import csv

class DAOBase:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.arquivo_original = arquivo

    def _abrir_arquivo(self, modo='r'):

        return open(self.arquivo, mode=modo, newline='', encoding='utf-8')

    def _escrever_cabecalho(self, file, cabecalho):
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(cabecalho)

    def _escrever_linha(self, file, linha):
        writer = csv.writer(file)
        writer.writerow(linha)

    def _ler_arquivo(self):
        with self._abrir_arquivo('r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def _salvar_todos(self, cabecalho, dados):
        with self._abrir_arquivo('w') as file:
            writer = csv.writer(file)
            writer.writerow(cabecalho)
            for dado in dados:
                writer.writerow(dado)

    def set_arquivo(self, novo_arquivo):
        self.arquivo = novo_arquivo

    def restaurar_arquivo_original(self):
        self.arquivo = self.arquivo_original