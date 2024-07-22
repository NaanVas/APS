import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.livro_controller import LivroController

class TelaCadastroLivro(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Cadastrar Livro")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.livro_controller = LivroController()

        label_titulo = tk.Label(self.frame_central, text="Cadastrar Livro", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Título:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_titulo = tk.Entry(self.frame_central)
        self.entry_titulo.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_central, text="Autor:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=2, column=0, pady=5, sticky='e')
        self.entry_autor = tk.Entry(self.frame_central)
        self.entry_autor.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_central, text="Editora:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=3, column=0, pady=5, sticky='e')
        self.entry_editora = tk.Entry(self.frame_central)
        self.entry_editora.grid(row=3, column=1, pady=5)

        tk.Label(self.frame_central, text="Ano de Publicação:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=4, column=0, pady=5, sticky='e')
        self.entry_ano = tk.Entry(self.frame_central)
        self.entry_ano.grid(row=4, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=5, column=0, columnspan=2, pady=10)

        self.botao_salvar = ttk.Button(self.frame_central, text="Salvar", style="Estilo.TButton", command=self.cadastrar_livro)
        self.botao_salvar.grid(row=6, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=6, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def cadastrar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        editora = self.entry_editora.get()
        ano = self.entry_ano.get()

        if titulo and autor and editora and ano:
            resultado = self.livro_controller.cadastrar_livro(titulo, autor, editora, ano)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Livro '{titulo}' cadastrado com sucesso.")
                self.limpar_campos()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_titulo.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

