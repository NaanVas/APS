from controle.autor_controller import AutorController
from visao.autor_view import AutorView
from controle.livro_controller import LivroController
from visao.livro_view import LivroView


def main():
    autor_controller = AutorController()
    autor_view = AutorView()
    livro_controller = LivroController()
    livro_view = LivroView()


    # Adicionar autores
    autor_controller.cadastrar_autor('Stephen King', 'Estados Unidos', '21/09/1947')
    autor_controller.cadastrar_autor('J.K. Rowling', 'Reino Unido', '31/07/1965')
    autor_controller.cadastrar_autor('Machado de Assis', 'Brasil', '21/06/1839')

    # Listar autores
    print("Lista de autores:")
    autores = autor_controller.listar_autores()
    for autor in autores:
        autor_view.imprimir_autor(autor)

    # Remover autor
    autor_controller.excluir_autor('Machado de Assis')

    # Buscar autor
    autor_buscado = autor_controller.buscar_autor('Stephen King')
    if autor_buscado:
        autor_view.imprimir_autor(autor_buscado)
    else:
        print("Autor não encontrado.")

    # Adicionar livros com autores cadastrados
    livro_controller.cadastrar_livro('It', 'Stephen King', 'Editora X', '1986')
    livro_controller.cadastrar_livro('Harry Potter', 'J.K. Rowling', 'Editora Y', '1997')

    # Adicionar livro sem autor cadastrado
    livro_controller.cadastrar_livro('Dom Casmurro', 'Machado de Assis', 'Editora Z', '1899')
    livro_controller.cadastrar_livro('1984', 'George Orwell', 'Secker & Warburg', '1949')


    # Listar livros
    print("\nLista de livros:")
    livros = livro_controller.listar_livros()
    for livro in livros:
            livro_view.imprimir_livro(livro)

    # Remover livro
    livro_controller.excluir_livro('Dom Casmurro')

    # Buscar livro
    livro_buscado = livro_controller.buscar_livro('It')
    if livro_buscado:
        livro_view.imprimir_livro(livro_buscado)
    else:
        print("\nLivro nao encontrado.")
    
    #cadastar autor que so tem o nome cadastrado
    autor_controller.cadastrar_autor('Machado de Assis', 'Brasil', '21/06/1839')
    
    # Remover autor
    autor_controller.excluir_autor('Stephen King')

if __name__ == "__main__":
    main()