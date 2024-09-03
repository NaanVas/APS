from persistencia.dao_base import DAOBase
from modelo.funcionario import Funcionario

class FuncionarioDAO(DAOBase):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FuncionarioDAO, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            super().__init__('funcionarios.csv')
            self._initialized = True

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
        print(f"Funcionário '{funcionario.get_nome()}' salvo com sucesso no arquivo CSV.")
    
    def excluir_funcionario(self, cpf):
        funcionarios = self.listar_funcionarios()
        funcionarios_filtrados = [f for f in funcionarios if f.get_cpf() != cpf]
        self._salvar_todos_funcionarios(funcionarios_filtrados)
        print(f"Funcionário com CPF '{cpf}' excluído com sucesso.")
    
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
