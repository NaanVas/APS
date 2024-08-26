from datetime import datetime
from modelo.emprestimo import Emprestimo
from controle.livro_controller import LivroController
from persistencia.dao_base import DAOBase

class EmprestimoDAO(DAOBase):
    def __init__(self, arquivo='emprestimos.csv', arquivo_devolucoes='devolucoes.csv'):
        super().__init__(arquivo)
        self.arquivo_devolucoes = arquivo_devolucoes
        self.livro_controller = LivroController()

    def criar_emprestimo(self, cpf_funcionario, cpf_usuario):
        return Emprestimo(cpf_funcionario, cpf_usuario)

    def adicionar_livro(self, emprestimo, livro):
        livros_atualizados = emprestimo.get_livros()
        livros_atualizados.append(livro)
        emprestimo.set_livros(livros_atualizados)

    def remover_livro(self, emprestimo, livro):
        livros_atualizados = emprestimo.get_livros()
        livros_atualizados.remove(livro)
        emprestimo.set_livros(livros_atualizados)

    def listar_livros(self, emprestimo):
        return emprestimo.get_livros()

    def aprovar_emprestimo(self, emprestimo):
        livros = self.livro_controller.listar_livros()
        for livro in emprestimo.get_livros():
            for l in livros:
                if livro.get_titulo() == l.get_titulo():
                    l.set_emprestado(True)
        self.livro_controller._salvar_todos_livros(livros)

        data_emprestimo = (emprestimo.get_data_emprestimo().strftime('%Y-%m-%d %H:%M:%S')
                           if emprestimo.get_data_emprestimo() else '')
        data_devolucao = (emprestimo.get_data_devolucao().strftime('%Y-%m-%d')
                          if emprestimo.get_data_devolucao() else '')

        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, [
                'CPF Funcionário', 'CPF Usuário', 'Livros', 'Data Empréstimo', 'Data Devolução', 'Status'
            ])
            self._escrever_linha(file, [
                emprestimo.get_cpf_funcionario(),
                emprestimo.get_cpf_usuario(),
                ', '.join([livro.get_titulo() for livro in emprestimo.get_livros()]),
                data_emprestimo,
                data_devolucao,
                emprestimo.get_status()
            ])

    def listar_emprestimos(self,):
        emprestimos = []
        for row in self._ler_arquivo():
            cpf_funcionario = row['CPF Funcionário']
            cpf_usuario = row['CPF Usuário']
            livros = row['Livros']
            data_emprestimo = row['Data Empréstimo']
            data_devolucao = row['Data Devolução']
            status = row['Status']

            livros_lista = livros.split(', ') if livros else []

            emprestimo = Emprestimo(cpf_funcionario, cpf_usuario, status)
            emprestimo.set_livros(livros_lista)
            emprestimo.set_data_emprestimo(datetime.strptime(data_emprestimo, '%Y-%m-%d %H:%M:%S') if data_emprestimo else None)
            emprestimo.set_data_devolucao(datetime.strptime(data_devolucao, '%Y-%m-%d') if data_devolucao else None)
            emprestimo.set_status(status)

            emprestimos.append(emprestimo)

        return emprestimos

    def buscar_emprestimo_pendente(self, cpf):
        emprestimos = self.listar_emprestimos()
        
        for emprestimo in emprestimos:
            if emprestimo.get_cpf_usuario() == cpf and emprestimo.get_status() == True:
                return f"O usuário '{cpf}' possui empréstimos em aberto."
        return None
    
    def registrar_devolucao(self, emprestimo, li, data_devolvida, multa):
        livros = self.livro_controller.listar_livros()

        for livro in livros:
            if livro.get_titulo() == li.get_titulo():
                livro.set_emprestado(False)

        self.livro_controller._salvar_todos_livros(livros)
        todos_livros = []
        for livro in emprestimo.get_livros():
            for l in livros:
                if livro == l.get_titulo():
                    todos_livros.append(l)

        todos_devolvidos = all(not livro.is_emprestado() for livro in todos_livros)
        if todos_devolvidos:
            emprestimos = self.listar_emprestimos()
            for emprest in emprestimos:
                if emprest.get_cpf_usuario() == emprestimo.get_cpf_usuario():
                    emprest.set_status(False)
            self._salvar_todos_emprestimos(emprestimos)
        
        self.set_arquivo(self.arquivo_devolucoes)

        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, [
                'CPF Funcionário', 'CPF Usuário', 'Título Livro', 'Data Devolução', 'Data Devolvida', 'Multa'
            ])
            self._escrever_linha(file, [
                emprestimo.get_cpf_funcionario(),
                emprestimo.get_cpf_usuario(),
                li.get_titulo(),
                emprestimo.get_data_devolucao().strftime('%Y-%m-%d') if emprestimo.get_data_devolucao() else '',
                data_devolvida.strftime('%Y-%m-%d'),
                multa if multa is not None else ''
            ])
        
        self.restaurar_arquivo_original()

    def _salvar_todos_emprestimos(self, emprestimos):
        cabecalho = [
            'CPF Funcionário', 'CPF Usuário', 'Livros', 'Data Empréstimo', 'Data Devolução', 'Status'
        ]
        dados = [
            [
                emprestimo.get_cpf_funcionario(),
                emprestimo.get_cpf_usuario(),
                ', '.join([livro for livro in emprestimo.get_livros()]),
                emprestimo.get_data_emprestimo().strftime('%Y-%m-%d %H:%M:%S') if emprestimo.get_data_emprestimo() else '',
                emprestimo.get_data_devolucao().strftime('%Y-%m-%d') if emprestimo.get_data_devolucao() else '',
                'True' if emprestimo.get_status() else 'False'
            ]
            for emprestimo in emprestimos
        ]
        self._salvar_todos(cabecalho, dados)
