import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.livro.cadastro import TelaCadastroLivro
from visao.tela.livro.excluir import TelaExcluirLivro
from visao.tela.livro.listar import TelaListarLivros
from visao.tela.livro.buscar import TelaBuscarLivro

class TelaInicialLivro(TelaPadrao):
    def __init__(self, root, voltar_callback, tipo_usuario):
        super().__init__(root, "Menu de Livros")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.janela_listar_aberta = None

        label_titulo = tk.Label(self.frame_central, text="Menu de Livros", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

        if tipo_usuario == 'funcionario':
            self.menu_funcionario()
        else:
            self.menu_usuario()

    def menu_usuario(self):
        botao_buscar = ttk.Button(self.frame_botoes, text="Buscar Livro", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_botoes, text="Listar Livros",style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar",style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

    def menu_funcionario(self):        

        botao_buscar = ttk.Button(self.frame_botoes, text="Buscar Livro", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_botoes, text="Listar Livros",style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_cadastrar = ttk.Button(self.frame_botoes, text="Cadastrar Livro",style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_botoes, text="Excluir Livro",style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar",style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

    def voltar_tela_livro(self):
        self.janela.deiconify()

    def abrir_tela_cadastrar(self):
        self.janela.withdraw()
        self.janela_cadastro = TelaCadastroLivro(self.root, self.voltar_tela_livro)

    def abrir_tela_excluir(self):
        self.janela.withdraw()
        self.janela_excluir = TelaExcluirLivro(self.root, self.voltar_tela_livro)

    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarLivros(self.root)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        self.janela_buscar = TelaBuscarLivro(self.root, self.voltar_tela_livro)
        
    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()
