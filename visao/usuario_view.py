from controle.usuario_controller import UsuarioController

class UsuarioView:
    def __init__(self):
        self.usuario_controller = UsuarioController()

    def listar_e_imprimir_usuarios(self):
        usuarios = self.usuario_controller.listar_usuarios()
        for usuario in usuarios:
            self.imprimir_usuario(usuario)

    def imprimir_usuario(self, usuario):
        print(f"CPF: {usuario.get_cpf()}")
        print(f"Nome: {usuario.get_nome()}")
        print(f"Tipo: {usuario.get_tipo()}")
        print()

    def imprimir_usuario_por_cpf(self, cpf):
        usuario = self.usuario_controller.buscar_usuario(cpf)
        if usuario:
            self.imprimir_usuario(usuario)
        else:
            print(f"Usuário com CPF '{cpf}' não encontrado.")

    def cadastrar_usuario(self, cpf, nome, senha, tipo):
        resultado = self.usuario_controller.cadastrar_usuario(cpf, nome, senha, tipo)
        if resultado:
            print(resultado)
        else:
            print(f"Usuário '{nome}' cadastrado com sucesso.")

    def excluir_usuario(self, cpf):
        resultado = self.usuario_controller.excluir_usuario(cpf)
        if resultado:
            print(resultado)
        else:
            print(f"Usuário com CPF '{cpf}' excluído com sucesso.")
