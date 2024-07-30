from modelo.funcionario import Funcionario
from persistencia.funcionario_dao import FuncionarioDAO
import datetime

class FuncionarioController:
    def __init__(self):
        self.funcionario_dao = FuncionarioDAO()

    def cadastrar_funcionario(self, cpf, nome, data_nascimento, salario, senha):
        try:
            cpf_int = int(cpf.replace(".", "").replace("-", ""))
        except ValueError:
            return "CPF inválido. Deve conter apenas números."

        try:
            datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        ano_atual = datetime.datetime.now().year
        data_nascimento_obj = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento_obj.year >= ano_atual:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        try:
            salario = float(salario)
            if salario < 0:
                return "O salário deve ser um número positivo."
        except ValueError:
            return "Salário inválido. Deve ser um número."
        
        if self.funcionario_dao.buscar_funcionario(cpf_int) is not None:
            return f"Funcionário com CPF '{cpf_int}' já cadastrado."
        
        novo_funcionario = Funcionario(cpf_int, nome, senha, data_nascimento, salario)
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
