class Emprestimo:
    def __init__(self, cpf_funcionario, cpf_usuario, status=True):
        self.cpf_funcionario = cpf_funcionario
        self.cpf_usuario = cpf_usuario
        self.livros = []
        self.data_emprestimo = None
        self.data_devolucao = None
        self.status = status

    def get_cpf_funcionario(self):
        return self.cpf_funcionario

    def set_cpf_funcionario(self, cpf_funcionario):
        self.cpf_funcionario = cpf_funcionario

    def get_cpf_usuario(self):
        return self.cpf_usuario

    def set_cpf_usuario(self, cpf_usuario):
        self.cpf_usuario = cpf_usuario

    def get_livros(self):
        return self.livros

    def set_livros(self, livros):
        self.livros = livros

    def get_data_emprestimo(self):
        return self.data_emprestimo

    def set_data_emprestimo(self, data_emprestimo):
        self.data_emprestimo = data_emprestimo

    def get_data_devolucao(self):
        return self.data_devolucao

    def set_data_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
