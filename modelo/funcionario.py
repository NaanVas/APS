from modelo.usuario import Usuario

class Funcionario(Usuario):
    def __init__(self, cpf, nome, senha, data_nascimento, salario):
        super().__init__(cpf, nome, senha, data_nascimento)
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario
