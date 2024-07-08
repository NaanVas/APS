import csv
from modelo.funcionario import Funcionario

class FuncionarioDAO:
    def __init__(self):
        self.arquivo_csv = "funcionarios.csv"

    def salvar_funcionario(self, funcionario):
        with open(self.arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['CPF', 'Nome', 'Senha', 'DataNascimento', 'Salario'])
            writer.writerow([funcionario.get_cpf(), funcionario.get_nome(), funcionario.get_senha(), funcionario.get_data_nascimento(), funcionario.get_salario()])
        print(f"Funcionário '{funcionario.get_nome()}' salvo com sucesso no arquivo CSV")
    
    def excluir_funcionario(self, cpf):
        funcionarios = self.listar_funcionarios()
        funcionarios_filtrados = [f for f in funcionarios if f.get_cpf() != cpf]
        self._salvar_todos_funcionarios(funcionarios_filtrados)
        print(f"Funcionário com CPF '{cpf}' excluído com sucesso")
    
    def buscar_funcionario(self, cpf):
        with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['CPF'] == cpf:
                    return Funcionario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'], row['Salario'])
        return None

    def listar_funcionarios(self):
        funcionarios = []
        with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                funcionario = Funcionario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'], row['Salario'])
                funcionarios.append(funcionario)
        return funcionarios
    
    def _salvar_todos_funcionarios(self, funcionarios):
        with open(self.arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['CPF', 'Nome', 'Senha', 'DataNascimento', 'Salario'])
            for funcionario in funcionarios:
                writer.writerow([funcionario.get_cpf(), funcionario.get_nome(), funcionario.get_senha(), funcionario.get_data_nascimento(), funcionario.get_salario()])
