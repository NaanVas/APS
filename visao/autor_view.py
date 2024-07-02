from controle.autor_controller import AutorController

class AutorView:
    def __init__(self):
        self.autor_controller = AutorController()

    def listar_e_imprimir_autores(self):
        autores = self.autor_controller.listar_autores()
        for autor in autores:
            self.imprimir_autor(autor)

    def imprimir_autor(self, autor):
        print(f"Nome: {autor.get_nome()}")
        print(f"Nacionalidade: {autor.get_nacionalidade()}")
        print()

    def imprimir_autor_por_nome(self, nome):
        autor = self.autor_controller.buscar_autor(nome)
        if autor:
            self.imprimir_autor(autor)
        else:
            print(f"Autor com nome '{nome}' nao encontrado.")