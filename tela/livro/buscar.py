import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.livro_controller import LivroController

class TelaBuscarLivro(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Buscar Livro")
        self.voltar_callback = voltar_callback
        self.livro_controller = LivroController()

        label_titulo = tk.Label(self.frame_central, text="Buscar Livro", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Título:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_titulo = tk.Entry(self.frame_central)
        self.entry_titulo.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 10), fg="red", bg="#F0DAAE")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_buscar = ttk.Button(self.frame_central, text="Buscar", style="Estilo.TButton", command=self.buscar_livro)
        botao_buscar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def buscar_livro(self):
        titulo = self.entry_titulo.get()
        if titulo:
            livro = self.livro_controller.buscar_livro(titulo)
            if livro:
                self.exibir_resultado_busca(livro)
            else:
                self.exibir_mensagem_erro(f"Livro com título '{titulo}' não encontrado.")
        else:
            self.exibir_mensagem_erro("Digite o título do livro.")

    def exibir_resultado_busca(self, livro):
        resultado = f"Título: {livro.get_titulo()}\n" \
                    f"Autor: {livro.get_autor()}\n" \
                    f"Editora: {livro.get_editora()}\n" \
                    f"Ano de Publicação: {livro.get_ano_publicacao()}"

        self.label_mensagem.config(text=resultado, fg="black")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")