import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.tela_inicial import TelaInicial
from controle.usuario_controller import UsuarioController
from controle.funcionario_controller import FuncionarioController

class TelaLogin(TelaPadrao):
    def __init__(self, root):
        super().__init__(root, "Login")
        self.janela.focus_set()
        self.usuario_controller = UsuarioController()
        self.funcionario_controller = FuncionarioController()
        
        self.label_titulo = tk.Label(self.frame_central, text="Login", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.label_cpf = tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#893F04",bg="#E5E0D8").grid(row=1, column=0, pady=5, padx=15, sticky='e')
        self.entry_cpf = ttk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, sticky="ew")

        self.label_senha = tk.Label(self.frame_central, text="Senha:", font=("Montserrat", 10), fg="#893F04",bg="#E5E0D8").grid(row=2, column=0, pady=5, padx=15, sticky='e')
        self.entry_senha = ttk.Entry(self.frame_central, show="*")
        self.entry_senha.grid(row=2, column=1, sticky="ew")

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="red", bg="#E5E0D8")
        self.label_mensagem.grid(row=3, column=0, columnspan=2, pady=10)

        self.frame_botoes.grid(row=4, column=0, columnspan=2, pady=2)
        self.botao_login = ttk.Button(self.frame_botoes, text="Login", style="Estilo.TButton", command=self.verificar_login)
        self.botao_login.grid(row=4, column=0, pady=10, padx=10)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela_login)

    def verificar_login(self):
        cpf = self.entry_cpf.get()
        senha = self.entry_senha.get()

        if not cpf or not senha:
            self.exibir_mensagem_erro("Por favor, preencha todos os campos.")
            return

        usuario = self.usuario_controller.buscar_usuario(cpf)
        funcionario = self.funcionario_controller.buscar_funcionario(cpf)

        if (usuario and usuario.get_senha() == senha):
            self.janela.withdraw()
            self.janela_inicial = TelaInicial(self.root, self.voltar_tela_login, 'user', cpf)
            self.limpar_campos()
        
        elif funcionario and funcionario.get_senha() == senha:
            self.janela.withdraw()
            self.janela_inicial = TelaInicial(self.root, self.voltar_tela_login, 'funcionario', cpf)
            self.limpar_campos()

        else:
            self.exibir_mensagem_erro("CPF ou senha incorretos.")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)

    def voltar_tela_login(self):
        self.janela.deiconify()

    def fechar_tela_login(self):
        self.janela.destroy()
        self.root.destroy()