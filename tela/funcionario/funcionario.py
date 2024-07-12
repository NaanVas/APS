import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from tela.funcionario.cadastro import TelaCadastroFuncionario
from tela.funcionario.excluir import TelaExcluirFuncionario
from tela.funcionario.listar import TelaListarFuncionarios
from tela.funcionario.buscar import TelaBuscarFuncionario
from controle.funcionario_controller import FuncionarioController

class TelaInicialFuncionario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Gerenciamento de Funcionários")
        self.voltar_callback = voltar_callback
        self.funcionario_controller = FuncionarioController()
        self.janela_listar_aberta = False

        label_titulo = tk.Label(self.frame_central, text="Tela de Gerenciamento de Funcionários", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        botao_cadastrar = ttk.Button(self.frame_central, text="Cadastrar Funcionário", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_central, text="Excluir Funcionário", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_central, text="Listar Funcionários", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_buscar = ttk.Button(self.frame_central, text="Buscar Funcionário", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
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
        self.janela_listar = TelaListarFuncionarios(self.root, self.voltar_tela_funcionario)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        self.janela_buscar = TelaBuscarFuncionario(self.root, self.voltar_tela_funcionario)
