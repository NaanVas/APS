import tkinter as tk
from tkinter import ttk
from controle.emprestimo_controller import EmprestimoController
from visao.tela.emprestimo.listar_emprestimos import TelaListarEmprestimos
from visao.tela.tela_padrao import TelaPadrao

class TelaVerificarEmprestimo(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Verificar Empréstimo")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.emprestimo_controller = EmprestimoController()
        self.janela_listar_aberta = None


        # Configuração da tela
        label_titulo = tk.Label(self.frame_central, text="Verificar Empréstimo", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF do Usuário:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_cpf_usuario = tk.Entry(self.frame_central)
        self.entry_cpf_usuario.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_verificar = ttk.Button(self.frame_central, text="Verificar", style="Estilo.TButton", command=self.verificar_emprestimo)
        botao_verificar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def verificar_emprestimo(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarEmprestimos(self.root, self.entry_cpf_usuario.get())

    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()
