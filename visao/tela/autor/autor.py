import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.autor.cadastro import TelaCadastroAutor
from visao.tela.autor.excluir import TelaExcluirAutor
from visao.tela.autor.listar import TelaListarAutores
from visao.tela.autor.buscar import TelaBuscarAutor

class TelaInicialAutor(TelaPadrao):
    def __init__(self, root, voltar_callback, tipo_usuario):
        super().__init__(root, "Gerenciamento de Autores")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.janela_listar_aberta = None

        label_titulo = tk.Label(self.frame_central, text="Tela de Gerenciamento de Autores", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

        if tipo_usuario == 'funcionario':
            self.menu_funcionario()
        else:
            self.menu_usuario()

    def menu_usuario(self):
        botao_buscar = ttk.Button(self.frame_botoes, text="Buscar Autor", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_botoes, text="Listar Autores", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

    def menu_funcionario(self):  
        botao_buscar = ttk.Button(self.frame_botoes, text="Buscar Autor", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_botoes, text="Listar Autores", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_cadastrar = ttk.Button(self.frame_botoes, text="Cadastrar Autor", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_botoes, text="Excluir Autor", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()

    def abrir_tela_cadastrar(self):
        self.janela.withdraw()
        self.janela_cadastro = TelaCadastroAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        self.janela_buscar = TelaBuscarAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_excluir(self):
        self.janela.withdraw()
        self.janela_excluir = TelaExcluirAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarAutores(self.root, self.voltar_para_tela_autor)

    def voltar_para_tela_autor(self):
        self.janela.deiconify()
