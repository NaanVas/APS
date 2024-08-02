from datetime import datetime, timedelta
from controle.funcionario_controller import FuncionarioController
from persistencia.emprestimo_dao import EmprestimoDAO
from controle.usuario_controller import UsuarioController
from controle.livro_controller import LivroController

class EmprestimoController:
    def __init__(self):
        self.emprestimo_dao = EmprestimoDAO()
        self.usuario_controller = UsuarioController()
        self.funcionario_controller = FuncionarioController()
        self.livro_controller = LivroController()

    def iniciar_emprestimo(self, cpf_funcionario, cpf_usuario):

        usuario_existe = self.usuario_controller.buscar_usuario(cpf_usuario)
        if usuario_existe is None:
            return f"Usuário com CPF '{cpf_usuario}' não encontrado."

        # Cria um novo objeto de empréstimo
        emprestimo = self.emprestimo_dao.criar_emprestimo(cpf_funcionario, cpf_usuario)
        return emprestimo

    def adicionar_livro(self, emprestimo, titulo):
        # Verifica se o livro já está no vetor
        for livro in emprestimo.get_livros():
            if livro.get_titulo() == titulo:
                return f"O livro '{titulo}' já foi adicionado ao empréstimo."
        
        # Verifica se o vetor de livros não atingiu o limite
        if len(emprestimo.get_livros()) >= 5:
            return f"O limite de 5 livros foi atingido."
        
        # Busca o livro pelo título usando o método do LivroController
        livro = self.livro_controller.buscar_livro(titulo)
        if livro is None:
            return f"Livro '{titulo}' não encontrado na biblioteca."

        # Adiciona o livro
        self.emprestimo_dao.adicionar_livro(emprestimo, livro)
        return None

    def remover_livro(self, emprestimo, titulo):
        # Verifica se o livro está no vetor de objetos Livro
        livro_encontrado = None
        for livro in emprestimo.get_livros():
            if livro.get_titulo() == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado is None:
            return f"Livro '{titulo}' não encontrado no empréstimo."

        # Remove o livro
        self.emprestimo_dao.remover_livro(emprestimo, livro_encontrado)
        return None

    def aprovar_emprestimo(self, emprestimo):
        # Verifica se há pelo menos um livro no empréstimo
        if len(emprestimo.get_livros()) == 0:
            return f"Não há livros no empréstimo para aprovar."

        # Define as datas de empréstimo e devolução
        emprestimo.set_data_emprestimo(datetime.now())
        emprestimo.set_data_devolucao(emprestimo.get_data_emprestimo() + timedelta(days=7))

        # Aprova o empréstimo
        self.emprestimo_dao.aprovar_emprestimo(emprestimo)
        return None

    def listar_livros(self, emprestimo):
        return self.emprestimo_dao.listar_livros(emprestimo)
    
    def buscar_data_pendente(self, cpf):
        return self.emprestimo_dao.buscar_data_pendente(cpf)

    def listar_emprestimos(self):
        return self.emprestimo_dao.listar_emprestimos()

    
