from persistencia.dao_base import DAOBase
from modelo.funcionario import Funcionario

class FuncionarioDAO(DAOBase):
    def __init__(self):
        super().__init__('funcionarios.csv')

    def salvar_funcionario(self, funcionario):
        cabecalho = ['CPF', 'Nome', 'Senha', 'DataNascimento', 'Salario']
        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, cabecalho)
            self._escrever_linha(file, [
                funcionario.get_cpf(), 
                funcionario.get_nome(), 
                funcionario.get_senha(), 
                funcionario.get_data_nascimento(), 
                funcionario.get_salario()
            ])
    
    def excluir_funcionario(self, cpf):
        funcionarios = self.listar_funcionarios()
        funcionarios_filtrados = [f for f in funcionarios if f.get_cpf() != cpf]
        self._salvar_todos_funcionarios(funcionarios_filtrados)
    
    def buscar_funcionario(self, cpf):
        funcionarios = self._ler_arquivo()
        for row in funcionarios:
            if row['CPF'] == cpf:
                return Funcionario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'], row['Salario'])
        return None

    def listar_funcionarios(self):
        funcionarios = []
        for row in self._ler_arquivo():
            funcionario = Funcionario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'], row['Salario'])
            funcionarios.append(funcionario)
        return funcionarios
    
    def _salvar_todos_funcionarios(self, funcionarios):
        cabecalho = ['CPF', 'Nome', 'Senha', 'DataNascimento', 'Salario']
        dados = [
            [funcionario.get_cpf(), funcionario.get_nome(), funcionario.get_senha(), funcionario.get_data_nascimento(), funcionario.get_salario()]
            for funcionario in funcionarios
        ]
        self._salvar_todos(cabecalho, dados)
