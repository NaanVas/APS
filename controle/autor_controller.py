from modelo.autor import Autor
from persistencia.autor_dao import AutorDAO
import datetime

class AutorController:
    def __init__(self):
        self.autor_dao = AutorDAO()

    def cadastrar_autor(self, nome, nacionalidade, data_nascimento):
        try:
            datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        ano_atual = datetime.datetime.now().year
        data_nascimento_obj = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento_obj.year >= ano_atual:
            return "Data de nascimento inválida. Use o formato DD/MM/AAAA"
        
        autor = self.autor_dao.buscar_autor(nome)
        if autor:
            if not autor.get_nacionalidade():
                autor.set_nacionalidade(nacionalidade)
                autor.set_data_nascimento(data_nascimento)
            else:
                return f"O autor '{autor.get_nome()} já existe."
            
            self.autor_dao.excluir_autor(nome)
            self.autor_dao.salvar_autor(autor)

            print(f"Autor '{autor.get_nome()}' já existe. Dados atualizados.")
            return None
        else:
            novo_autor = Autor(nome, nacionalidade, data_nascimento) 
            self.autor_dao.salvar_autor(novo_autor)  
            return None

    def excluir_autor(self, nome):
        autor = self.autor_dao.buscar_autor(nome)
        if autor:
            self.autor_dao.excluir_autor(nome)
            return None
        else:
            return f"Autor '{nome} não encontrado."

    def buscar_autor(self, nome):
        return self.autor_dao.buscar_autor(nome)

    def listar_autores(self):
        return self.autor_dao.listar_autores()