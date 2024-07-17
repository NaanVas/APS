import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.autor_controller import AutorController

class TelaCadastroAutor(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Cadastrar Autor")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.autor_controller = AutorController()

        label_titulo = tk.Label(self.frame_central, text="Cadastrar Autor", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Nome:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_nome = tk.Entry(self.frame_central)
        self.entry_nome.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_central, text="Nacionalidade:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=2, column=0, pady=5, sticky='e')
        self.entry_nacionalidade = tk.Entry(self.frame_central)
        self.entry_nacionalidade.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_central, text="Data de Nascimento:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=3, column=0, pady=5, sticky='e')
        self.entry_data_nascimento = tk.Entry(self.frame_central)
        self.entry_data_nascimento.grid(row=3, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=4, column=0, columnspan=2, pady=10)

        botao_salvar = ttk.Button(self.frame_central, text="Salvar", style="Estilo.TButton", command=self.cadastrar_autor)
        botao_salvar.grid(row=5, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=5, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def cadastrar_autor(self):
        nome = self.entry_nome.get()
        nacionalidade = self.entry_nacionalidade.get()
        data_nascimento = self.entry_data_nascimento.get()

        if nome and nacionalidade and data_nascimento:
            resultado = self.autor_controller.cadastrar_autor(nome, nacionalidade, data_nascimento)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Autor '{nome}' cadastrado com sucesso.")
                self.limpar_campos()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_nacionalidade.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_nome.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
