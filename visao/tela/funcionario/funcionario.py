import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.funcionario.cadastro import TelaCadastroFuncionario
from visao.tela.funcionario.excluir import TelaExcluirFuncionario
from visao.tela.funcionario.listar import TelaListarFuncionarios
from visao.tela.funcionario.buscar import TelaBuscarFuncionario

class TelaInicialFuncionario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Gerenciamento de Funcionários")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.janela_listar_aberta = None

        label_titulo = tk.Label(self.frame_central, text="Tela de Gerenciamento de Funcionários", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)

        botao_buscar = ttk.Button(self.frame_botoes, text="Buscar Funcionário", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_botoes, text="Listar Funcionários", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_cadastrar = ttk.Button(self.frame_botoes, text="Cadastrar Funcionário", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_botoes, text="Excluir Funcionário", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()

    def voltar_tela_funcionario(self):
        self.janela.deiconify()

    def abrir_tela_cadastrar(self):
        self.janela.withdraw()
        self.janela_cadastro = TelaCadastroFuncionario(self.root, self.voltar_tela_funcionario)

    def abrir_tela_excluir(self):
        self.janela.withdraw()
        self.janela_excluir = TelaExcluirFuncionario(self.root, self.voltar_tela_funcionario)

    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarFuncionarios(self.root, self.voltar_tela_funcionario)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        self.janela_buscar = TelaBuscarFuncionario(self.root, self.voltar_tela_funcionario)
