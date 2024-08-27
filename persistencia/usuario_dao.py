from persistencia.dao_base import DAOBase
from modelo.usuario import Usuario

class UsuarioDAO(DAOBase):
    def __init__(self):
        super().__init__("usuarios.csv")

    def salvar_usuario(self, usuario):
        cabecalho = ['CPF', 'Nome', 'Senha', 'DataNascimento']
        with self._abrir_arquivo(modo='a') as file:
            self._escrever_cabecalho(file, cabecalho)
            self._escrever_linha(file, [
                usuario.get_cpf(), 
                usuario.get_nome(), 
                usuario.get_senha(), 
                usuario.get_data_nascimento()
            ])
        print(f"Usuário '{usuario.get_nome()}' salvo com sucesso no arquivo CSV")
    
    def excluir_usuario(self, cpf):
        usuarios = self.listar_usuarios()
        usuarios_filtrados = [u for u in usuarios if u.get_cpf() != cpf]
        self._salvar_todos_usuarios(usuarios_filtrados)
        print(f"Usuário com CPF '{cpf}' excluído com sucesso")
    
    def buscar_usuario(self, cpf):
        usuarios = self._ler_arquivo()
        for row in usuarios:
            if row['CPF'] == cpf:
                return Usuario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'])
        return None

    def listar_usuarios(self):
        usuarios = []
        for row in self._ler_arquivo():
            usuario = Usuario(row['CPF'], row['Nome'], row['Senha'], row['DataNascimento'])
            usuarios.append(usuario)
        return usuarios
    
    def _salvar_todos_usuarios(self, usuarios):
        cabecalho = ['CPF', 'Nome', 'Senha', 'DataNascimento']
        dados = [
            [u.get_cpf(), u.get_nome(), u.get_senha(), u.get_data_nascimento()]
            for u in usuarios
        ]
        self._salvar_todos(cabecalho, dados)
