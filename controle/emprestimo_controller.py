from datetime import datetime, timedelta
from controle.funcionario_controller import FuncionarioController
from persistencia.emprestimo_dao import EmprestimoDAO
from controle.usuario_controller import UsuarioController
from controle.livro_controller import LivroController
from controle.Strategy.emprestimo_strategy import EmprestimoStrategy

class EmprestimoController:
    def __init__(self, strategy: EmprestimoStrategy):
        self.emprestimo_dao = EmprestimoDAO()
        self.usuario_controller = UsuarioController()
        self.funcionario_controller = FuncionarioController()
        self.livro_controller = LivroController()
        self.strategy = strategy

    def set_strategy(self, strategy: EmprestimoStrategy):
        self.strategy = strategy

    def iniciar_emprestimo(self, cpf_funcionario, cpf_usuario):

        usuario_existe = self.usuario_controller.buscar_usuario(cpf_usuario)
        if usuario_existe is None:
            return f"Usuário com CPF '{cpf_usuario}' não encontrado."

        emprestimo = self.emprestimo_dao.criar_emprestimo(cpf_funcionario, cpf_usuario)
        return emprestimo

    def adicionar_livro(self, emprestimo, titulo):
        for livro in emprestimo.get_livros():
            if livro is not None and livro.get_titulo() == titulo:
                return f"O livro '{titulo}' já foi adicionado ao empréstimo."
        
        if len(emprestimo.get_livros()) >= self.strategy.verificar_limite_livros():
            return f"O limite de {self.strategy.verificar_limite_livros()} livros foi atingido."
        
        livro = self.livro_controller.buscar_livro(titulo)
        if livro is None:
            return f"O livro '{titulo}' não foi encontrado no sistema."
        
        if livro.is_emprestado():
            return f"O livro '{livro.get_titulo()}' já está emprestado e não pode ser aprovado novamente."
        
        self.emprestimo_dao.adicionar_livro(emprestimo, livro)
        return None

    def remover_livro(self, emprestimo, titulo):
        livro_encontrado = None
        for livro in emprestimo.get_livros():
            if livro.get_titulo() == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado is None:
            return f"Livro '{titulo}' não encontrado no empréstimo."

        livro = self.livro_controller.buscar_livro(titulo)
        self.emprestimo_dao.remover_livro(emprestimo, livro)
        return None

    def aprovar_emprestimo(self, emprestimo):
        if len(emprestimo.get_livros()) == 0:
            return f"Não há livros no empréstimo para aprovar."

        emprestimo.set_data_emprestimo(datetime.now())
        emprestimo.set_data_devolucao(emprestimo.get_data_emprestimo() + self.strategy.calcular_periodo_emprestimo())

        livros = self.livro_controller.listar_livros()
        for livro in emprestimo.get_livros():
            for l in livros:
                if livro is not None and livro.get_titulo() == l.get_titulo():
                    l.set_emprestado(True)

        self.emprestimo_dao.salvar_emprestimo(emprestimo, livros)
        return None

    def listar_livros(self, emprestimo):
        return self.emprestimo_dao.listar_livros(emprestimo)
    
    def buscar_emprestimo_pendente(self, cpf):
        return self.emprestimo_dao.buscar_emprestimo_pendente(cpf)

    def listar_emprestimos(self):
        return self.emprestimo_dao.listar_emprestimos()
    
    def atualizar_status_livros_devolvidos(self, li):
        livros = self.livro_controller.listar_livros()
        for livro in livros:
            if livro.get_titulo() == li.get_titulo():
                livro.set_emprestado(False)
        self.livro_controller._salvar_todos_livros(livros)

    def verificar_todos_livros_devolvidos(self, emprestimo):
        todos_devolvidos = True
        for livro_emprestado in emprestimo.get_livros():
            livro = self.livro_controller.buscar_livro(livro_emprestado.get_titulo())
            if livro.is_emprestado():
                todos_devolvidos =  False
                break

        if todos_devolvidos:
            emprestimos = self.listar_emprestimos()
            for emprest in emprestimos:
                if emprest.get_cpf_usuario() == emprestimo.get_cpf_usuario():
                    emprest.set_status(False)
            self.emprestimo_dao._salvar_todos_emprestimos(emprestimos)

    def realizar_devolucao(self, cpf_usuario, titulo_livro):
        emprestimo_usuario = None
        emprestimos = self.emprestimo_dao.listar_emprestimos()
        for emprestimo in emprestimos:
            if emprestimo.get_cpf_usuario() == cpf_usuario:
                emprestimo_usuario = emprestimo
        if emprestimo_usuario == None:
            return f"Emprestimo para usuario '{cpf_usuario}' nao encontrado"
        
        livros = self.emprestimo_dao.listar_livros(emprestimo_usuario)
        livro = None
        for li in livros:
            if li.get_titulo() == titulo_livro:
                livro = titulo_livro

        if livro is not None:
            livro = self.livro_controller.buscar_livro(livro)
            if livro.is_emprestado():
                data_devolucao = emprestimo_usuario.get_data_devolucao()
                data_atual = datetime.now()
                if data_atual <= data_devolucao:
                    self.atualizar_status_livros_devolvidos(livro)
                    self.verificar_todos_livros_devolvidos(emprestimo_usuario)
                    self.emprestimo_dao.registrar_devolucao(emprestimo_usuario, livro, data_atual, None)
                    return None
                else:
                    atraso = (data_atual - data_devolucao).days
                    multa = self.strategy.calcular_multa(atraso)
                    self.atualizar_status_livros_devolvidos(livro)
                    self.verificar_todos_livros_devolvidos(emprestimo_usuario)
                    self.emprestimo_dao.registrar_devolucao(emprestimo_usuario, livro, data_atual, multa)
                    return None
            else:
                return f"Livro {titulo_livro} nao esta emprestado"
        else:
            return f"Livro '{titulo_livro}' nao encontrado no emprestimo"

