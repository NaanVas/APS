import csv
from datetime import datetime
from modelo.emprestimo import Emprestimo

class EmprestimoDAO:
    def __init__(self, arquivo='emprestimos.csv'):
        self.arquivo = arquivo

    def criar_emprestimo(self, cpf_funcionario, cpf_usuario):
        return Emprestimo(cpf_funcionario, cpf_usuario)

    def adicionar_livro(self, emprestimo, livro):
        # Adiciona o objeto Livro à lista usando um método da classe Emprestimo
        livros_atualizados = emprestimo.get_livros()
        livros_atualizados.append(livro)
        emprestimo.set_livros(livros_atualizados)

    def remover_livro(self, emprestimo, livro):
        # Remove o objeto Livro da lista usando um método da classe Emprestimo
        livros_atualizados = emprestimo.get_livros()
        livros_atualizados.remove(livro)
        emprestimo.set_livros(livros_atualizados)

    def listar_livros(self, emprestimo):
        return emprestimo.get_livros()

    def aprovar_emprestimo(self, emprestimo):
        # Verifica se as datas não são None antes de tentar formatar
        data_emprestimo = (emprestimo.get_data_emprestimo().strftime('%Y-%m-%d %H:%M:%S')
                           if emprestimo.get_data_emprestimo() else '')
        data_devolucao = (emprestimo.get_data_devolucao().strftime('%Y-%m-%d')
                          if emprestimo.get_data_devolucao() else '')

        with open(self.arquivo, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow([
                    'CPF Funcionário', 'CPF Usuário', 'Livros', 'Data Empréstimo', 'Data Devolução'
                ])
            writer.writerow([
                emprestimo.get_cpf_funcionario(),
                emprestimo.get_cpf_usuario(),
                ', '.join([livro.get_titulo() for livro in emprestimo.get_livros()]),
                data_emprestimo,
                data_devolucao
            ])
            
    def buscar_data_pendente(self, cpf):
        hoje = datetime.now().date()
        
        with open(self.arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['CPF Usuário'] == cpf:
                        data_devolucao_str = row['Data Devolução']
                        if data_devolucao_str:
                            data_devolucao = datetime.strptime(data_devolucao_str, '%Y-%m-%d').date()
                            if data_devolucao >= hoje:
                                return f"O usuário '{cpf}' possui emprestimos com data pendente para devolução"
                            
                            else:
                                return None
                            
    def listar_emprestimos(self):
        emprestimos = []
        with open(self.arquivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cpf_funcionario = row['CPF Funcionário']
                    cpf_usuario = row['CPF Usuário']
                    livros = row['Livros']
                    data_emprestimo = row['Data Empréstimo']
                    data_devolucao = row['Data Devolução']
                    
                    # Transformar livros em lista
                    livros_lista = livros.split(', ') if livros else []

                    # Criar objeto Emprestimo
                    emprestimo = Emprestimo(cpf_funcionario, cpf_usuario)
                    emprestimo.set_livros(livros_lista)  # Supondo que Emprestimo tenha esse método
                    emprestimo.set_data_emprestimo(datetime.strptime(data_emprestimo, '%Y-%m-%d %H:%M:%S') if data_emprestimo else None)
                    emprestimo.set_data_devolucao(datetime.strptime(data_devolucao, '%Y-%m-%d') if data_devolucao else None)

                    emprestimos.append(emprestimo)
        return emprestimos
    
    def buscar_data_pendente(self, cpf):
        hoje = datetime.now().date()
        emprestimos = self.listar_emprestimos()
        
        for emprestimo in emprestimos:
            if emprestimo.get_cpf_usuario() == cpf:
                data_devolucao = emprestimo.get_data_devolucao()
                if isinstance(data_devolucao, datetime):
                    data_devolucao = data_devolucao.date()
                
                if data_devolucao and data_devolucao >= hoje:
                    return f"O usuário '{cpf}' possui empréstimos com data pendente para devolução."
        
        return None