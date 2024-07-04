import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from tela.livro.cadastro import TelaCadastroLivro
from tela.livro.excluir import TelaExcluirLivro
from tela.livro.listar import TelaListarLivros
from tela.livro.buscar import TelaBuscarLivro

class TelaInicialLivro(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Menu de Livros")
        self.voltar_callback = voltar_callback

        label_titulo = tk.Label(self.frame_central, text="Menu de Livros", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Botões para navegar para outras telas
        botao_cadastrar = ttk.Button(self.frame_central, text="Cadastrar Livro",style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_central, text="Excluir Livro",style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_central, text="Listar Livros",style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        botao_buscar = ttk.Button(self.frame_central, text="Buscar Livro", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_central, text="Voltar",style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=5, column=0, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def voltar_tela_livro(self):
        self.janela.deiconify()

    def abrir_tela_cadastrar(self):
        self.janela.withdraw()
        self.janela_cadastro = TelaCadastroLivro(self.root, self.voltar_tela_livro)

    def abrir_tela_excluir(self):
        self.janela.withdraw()
        self.janela_excluir = TelaExcluirLivro(self.root, self.voltar_tela_livro)

    def abrir_tela_listar(self):
        self.janela_listar = TelaListarLivros(self.root, self.voltar_tela_livro)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        self.janela_buscar = TelaBuscarLivro(self.root, self.voltar_tela_livro)
        
    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
