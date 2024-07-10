import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from tela.autor.cadastro import TelaCadastroAutor
from tela.autor.excluir import TelaExcluirAutor
from tela.autor.listar import TelaListarAutores
from tela.autor.buscar import TelaBuscarAutor
from controle.autor_controller import AutorController

class TelaInicialAutor(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Gerenciamento de Autores")
        self.voltar_callback = voltar_callback
        self.autor_c = AutorController()

        label_titulo = tk.Label(self.frame_central, text="Tela de Gerenciamento de Autores", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        botao_cadastrar = ttk.Button(self.frame_central, text="Cadastrar Autor", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_buscar = ttk.Button(self.frame_central, text="Buscar Autor", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_excluir = ttk.Button(self.frame_central, text="Excluir Autor", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_central, text="Listar Autores", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=5, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def abrir_tela_cadastrar(self):
        self.janela.withdraw()
        TelaCadastroAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_buscar(self):
        self.janela.withdraw()
        TelaBuscarAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_excluir(self):
        self.janela.withdraw()
        TelaExcluirAutor(self.root, self.voltar_para_tela_autor)

    def abrir_tela_listar(self):
        self.janela.withdraw()
        TelaListarAutores(self.root, self.voltar_para_tela_autor)

    def voltar_para_tela_autor(self):
        self.janela.deiconify()
