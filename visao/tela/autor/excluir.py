import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.autor_controller import AutorController

class TelaExcluirAutor(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Excluir Autor")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.autor_controller = AutorController()

        label_titulo = tk.Label(self.frame_central, text="Excluir Autor", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Nome:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_excluir_nome = tk.Entry(self.frame_central)
        self.entry_excluir_nome.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_excluir = ttk.Button(self.frame_central, text="Excluir", style="Estilo.TButton", command=self.excluir_autor)
        botao_excluir.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
    
    def excluir_autor(self):
        nome = self.entry_excluir_nome.get()
        if nome:
            resultado = self.autor_controller.excluir_autor(nome)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Autor '{nome}' excluído com sucesso.")
                self.limpar_campos()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o nome do autor a ser excluído.")

    def limpar_campos(self):
        self.entry_excluir_nome.delete(0, tk.END)
        self.entry_excluir_nome.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
