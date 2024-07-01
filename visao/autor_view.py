from persistencia.autor_dao import AutorDAO

class AutorView:
    def __init__(self):
        self.autor_dao = AutorDAO()

    def listar_e_imprimir_autores(self):
        autores = self.autor_dao.listar_autores()
        for autor in autores:
            self.imprimir_autor(autor)

    def imprimir_autor(self, autor):
        print(f"Nome: {autor.get_nome()}")
        print(f"Nacionalidade: {autor.get_nacionalidade()}")
        print(f"Data de Nascimento: {autor.get_data_nascimento()}")
        print()

    def imprimir_autor_por_nome(self, nome):
        autor = self.autor_dao.buscar_autor(nome)
        if autor:
            self.imprimir_autor(autor)
        else:
            print(f"Autor com nome '{nome}' nao encontrado.")