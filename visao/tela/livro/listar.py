import tkinter as tk
from visao.tela.tela_padrao import TelaPadrao
from controle.livro_controller import LivroController

class TelaListarLivros(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Listagem de Livros")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.livro_controller = LivroController()
        self.text_area = None  

        self.janela.geometry("600x450+800+150")

        self.configurar_interface()

    def configurar_interface(self):
        self.janela_listar_aberta = True
        label_titulo = tk.Label(self.frame_central, text="Listagem de Livros", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        scrollbar = tk.Scrollbar(self.janela)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(self.janela, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#E5E0D8", font=("Montserrat", 10))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.text_area.yview)

        self.atualizar_lista()

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela_listar_aberta = False
        self.janela.destroy()
        self.voltar_callback()

    def listar_livros(self):
        return self.livro_controller.listar_livros()

    def atualizar_lista(self):
        if self.janela_listar_aberta and self.text_area:
            self.text_area.delete('1.0', tk.END) 

            livros = self.listar_livros()

            for livro in livros:
                titulo = f"Título: {livro.get_titulo()}\n"
                autor = f"Autor: {livro.get_autor()}\n"
                editora = f"Editora: {livro.get_editora()}\n"
                ano = f"Ano: {livro.get_ano_publicacao()}\n"

                self.text_area.insert(tk.END, titulo, "negrito")
                self.text_area.insert(tk.END, autor)
                self.text_area.insert(tk.END, editora)
                self.text_area.insert(tk.END, ano)
                self.text_area.insert(tk.END, "\n")

                self.text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))

