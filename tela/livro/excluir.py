import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.livro_controller import LivroController

class TelaExcluirLivro(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Excluir Livro")
        self.voltar_callback = voltar_callback
        self.livro_controller = LivroController()

        label_titulo = tk.Label(self.frame_central, text="Excluir Livro", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Título:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_excluir_titulo = tk.Entry(self.frame_central)
        self.entry_excluir_titulo.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        self.botao_salvar = ttk.Button(self.frame_central, text="Salvar", style="Estilo.TButton", command=self.excluir_livro)
        self.botao_salvar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def excluir_livro(self):
        titulo = self.entry_excluir_titulo.get()
        if titulo:
            resultado = self.livro_controller.excluir_livro(titulo)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Livro com título '{titulo}' excluído com sucesso.")
                self.entry_excluir_titulo.delete(0, tk.END)
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o título do livro.")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
