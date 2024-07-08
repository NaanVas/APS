from modelo.funcionario import Funcionario
from persistencia.funcionario_dao import FuncionarioDAO

class FuncionarioController:
    def __init__(self):
        self.funcionario_dao = FuncionarioDAO()

    def cadastrar_funcionario(self, cpf, nome, senha, data_nascimento, salario):
        if self.funcionario_dao.buscar_funcionario(cpf) is not None:
            return f"Funcionário com CPF '{cpf}' já cadastrado."
        
        novo_funcionario = Funcionario(cpf, nome, senha, data_nascimento, salario)
        self.funcionario_dao.salvar_funcionario(novo_funcionario)
        return None
    
    def excluir_funcionario(self, cpf):
        funcionario_existe = self.funcionario_dao.buscar_funcionario(cpf)
        if funcionario_existe is None:
            return f"Funcionário com CPF '{cpf}' não encontrado."

        self.funcionario_dao.excluir_funcionario(cpf)
        return None
    
    def buscar_funcionario(self, cpf):
        return self.funcionario_dao.buscar_funcionario(cpf)
    
    def listar_funcionarios(self):
        return self.funcionario_dao.listar_funcionarios()
