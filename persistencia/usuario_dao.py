import csv
from modelo.usuario import Usuario
from modelo.funcionario import Funcionario

class UsuarioDAO:
    def __init__(self):
        self.arquivo_csv = "usuarios.csv"

    def salvar_usuario(self, usuario):
        with open(self.arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['CPF', 'Nome', 'Senha', 'Tipo', 'Salario'])
            if isinstance(usuario, Funcionario):
                writer.writerow([usuario.get_cpf(), usuario.get_nome(), usuario.get_senha(), usuario.get_tipo(), usuario.get_salario()])
            else:
                writer.writerow([usuario.get_cpf(), usuario.get_nome(), usuario.get_senha(), usuario.get_tipo(), ''])
        print(f"Usuário '{usuario.get_nome()}' salvo com sucesso no arquivo CSV")
    
    def excluir_usuario(self, cpf):
        usuarios = self.listar_usuarios()
        usuarios_filtrados = [u for u in usuarios if u.get_cpf() != cpf]
        self._salvar_todos_usuarios(usuarios_filtrados)
        print(f"Usuário com CPF '{cpf}' excluído com sucesso")
    
    def buscar_usuario(self, cpf):
        with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['CPF'] == cpf:
                    if row['Salario']:
                        return Funcionario(row['CPF'], row['Nome'], row['Senha'], row['Tipo'], row['Salario'])
                    else:
                        return Usuario(row['CPF'], row['Nome'], row['Senha'], row['Tipo'])
        return None

    def listar_usuarios(self):
        usuarios = []
        with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Salario']:
                    usuario = Funcionario(row['CPF'], row['Nome'], row['Senha'], row['Tipo'], row['Salario'])
                else:
                    usuario = Usuario(row['CPF'], row['Nome'], row['Senha'], row['Tipo'])

                usuarios.append(usuario)
        return usuarios
    
    def _salvar_todos_usuarios(self, usuarios):
        with open(self.arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['CPF', 'Nome', 'Senha', 'Tipo', 'Salario'])
            for usuario in usuarios:
                if isinstance(usuario,Funcionario):
                    writer.writerow([usuario.get_cpf(), usuario.get_nome(), usuario.get_senha(), usuario.get_tipo(),usuario.get_salario()])
                else:
                    writer.writerow([usuario.get_cpf(), usuario.get_nome(), usuario.get_senha(), usuario.get_tipo(), ''])