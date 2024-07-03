from modelo.usuario import Usuario
from modelo.funcionario import Funcionario
from persistencia.usuario_dao import UsuarioDAO

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def cadastrar_usuario(self, cpf, nome, senha, tipo, salario=None):
        if self.usuario_dao.buscar_usuario(cpf) is not None:
            return f"Usuário com CPF '{cpf}' já cadastrado."
        
        if salario is not None:
            novo_usuario = Funcionario(cpf, nome, senha, tipo, salario)
        else:
            novo_usuario = Usuario(cpf, nome, senha, tipo)
            
        self.usuario_dao.salvar_usuario(novo_usuario)
        return None
    
    def excluir_usuario(self, cpf):
        usuario_existe = self.usuario_dao.buscar_usuario(cpf)
        if usuario_existe is None:
            return f"Usuário com CPF '{cpf}' não encontrado."

        self.usuario_dao.excluir_usuario(cpf)
        return None
    
    def buscar_usuario(self, cpf):
        return self.usuario_dao.buscar_usuario(cpf)
    
    def listar_usuarios(self):
        return self.usuario_dao.listar_usuarios()
    
    def verifica_tipo(self, cpf):
        usuario = self.usuario_dao.buscar_usuario(cpf)
        if usuario:
            if usuario.get_tipo() == 'admin':
                return "admin"
            else:
                return "user"
        else:
            return None
