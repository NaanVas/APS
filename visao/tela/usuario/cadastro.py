import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.usuario_controller import UsuarioController

class TelaCadastroUsuario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Cadastrar Usuário")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.usuario_controller = UsuarioController()

        label_titulo = tk.Label(self.frame_central, text="Cadastrar Usuário", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_central, text="Nome:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=2, column=0, pady=5, sticky='e')
        self.entry_nome = tk.Entry(self.frame_central)
        self.entry_nome.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_central, text="Data de Nascimento:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=3, column=0, pady=5, sticky='e')
        self.entry_data_nascimento = tk.Entry(self.frame_central)
        self.entry_data_nascimento.grid(row=3, column=1, pady=5)

        tk.Label(self.frame_central, text="Senha:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=4, column=0, pady=5, sticky='e')
        self.entry_senha = tk.Entry(self.frame_central, show="*")
        self.entry_senha.grid(row=4, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=5, column=0, columnspan=2, pady=10)

        self.botao_salvar = ttk.Button(self.frame_central, text="Salvar", style="Estilo.TButton", command=self.cadastrar_usuario)
        self.botao_salvar.grid(row=6, column=0, pady=10)

        self.botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        self.botao_voltar.grid(row=6, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
        
    def cadastrar_usuario(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        data_nascimento = self.entry_data_nascimento.get()

        if cpf and nome and senha and data_nascimento:
            resultado = self.usuario_controller.cadastrar_usuario(cpf, nome, data_nascimento, senha)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Usuário '{nome}' cadastrado com sucesso.")
                self.limpar_campos()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")

    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_cpf.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
