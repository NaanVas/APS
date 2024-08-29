from modelo.usuario import Usuario
from persistencia.usuario_dao import UsuarioDAO
import datetime

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def cadastrar_usuario(self, cpf, nome, data_nascimento, senha):
      
        try:
            datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        ano_atual = datetime.datetime.now().year
        data_nascimento_obj = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento_obj.year >= ano_atual:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        if self.usuario_dao.buscar_usuario(cpf) is not None:
            return f"Usuário com CPF '{cpf}' já cadastrado."
        
        novo_usuario = Usuario(cpf, nome, senha, data_nascimento)
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
