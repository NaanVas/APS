import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.livro.livro import TelaInicialLivro
from visao.tela.autor.autor import TelaInicialAutor
from visao.tela.usuario.usuario import TelaInicialUsuario
from visao.tela.funcionario.funcionario import TelaInicialFuncionario

class TelaInicial(TelaPadrao):
    def __init__(self, root, voltar_callback, tipo_usuario):
        super().__init__(root, "Sistema de Gerenciamento de Biblioteca")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback

        self.label_boas_vindas = tk.Label(self.frame_central, text="Bem-vindo ao Sistema de Biblioteca", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        self.label_boas_vindas.grid(row=0, column=0, columnspan=2, pady=20)

        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)


        if tipo_usuario == 'funcionario':
            self.menu_funcionario(tipo_usuario)
        else:
            self.menu_usuario(tipo_usuario)

    def menu_usuario(self, tipo_usuario):
        self.botao_livro = ttk.Button(self.frame_botoes, text="Livro", style="Estilo.TButton", command=lambda: self.abrir_tela_livro(tipo_usuario))
        self.botao_livro.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.botao_autor = ttk.Button(self.frame_botoes, text="Autor", style="Estilo.TButton", command=lambda: self.abrir_tela_autor(tipo_usuario))
        self.botao_autor.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        botao_sair = ttk.Button(self.frame_botoes, text="Sair", style="Estilo.TButton", command=self.fechar_tela)
        botao_sair.grid(row=2, column=0, pady=10, padx=10, sticky="ew")


    def menu_funcionario(self, tipo_usuario):
        self.botao_livro = ttk.Button(self.frame_botoes, text="Livro", style="Estilo.TButton", command=lambda: self.abrir_tela_livro(tipo_usuario))
        self.botao_livro.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.botao_autor = ttk.Button(self.frame_botoes, text="Autor", style="Estilo.TButton", command=lambda: self.abrir_tela_autor(tipo_usuario))
        self.botao_autor.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        self.botao_emprestimo = ttk.Button(self.frame_botoes, text="Empréstimo", style="Estilo.TButton", command=self.abrir_tela_emprestimo)
        self.botao_emprestimo.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        self.botao_devolucoes = ttk.Button(self.frame_botoes, text="Devoluções", style="Estilo.TButton", command=self.abrir_tela_devolucoes)
        self.botao_devolucoes.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        self.botao_usuario = ttk.Button(self.frame_botoes, text="Usuário", style="Estilo.TButton", command=self.abrir_tela_usuario)
        self.botao_usuario.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

        self.botao_funcionario = ttk.Button(self.frame_botoes, text="Funcionário", style="Estilo.TButton", command=self.abrir_tela_funcionario)
        self.botao_funcionario.grid(row=5, column=0, pady=10, padx=10, sticky="ew")

        botao_sair = ttk.Button(self.frame_botoes, text="Sair", style="Estilo.TButton", command=self.fechar_tela)
        botao_sair.grid(row=6, column=0, pady=10, padx=10, sticky="ew")

    def abrir_tela_livro(self, tipo_usuario):
        self.janela.withdraw()
        self.janela_livro = TelaInicialLivro(self.root, self.voltar_tela_inicial, tipo_usuario)

    def abrir_tela_autor(self, tipo_usuario):
        self.janela.withdraw()
        self.janela_autor = TelaInicialAutor(self.root, self.voltar_tela_inicial, tipo_usuario)

    def abrir_tela_emprestimo(self):
        pass

    def abrir_tela_devolucoes(self):
        pass

    def abrir_tela_usuario(self):
        self.janela.withdraw()
        self.janela_usuario = TelaInicialUsuario(self.root, self.voltar_tela_inicial)

    def abrir_tela_funcionario(self):
        self.janela.withdraw()
        self.janela_funcionario = TelaInicialFuncionario(self.root, self.voltar_tela_inicial)

    def voltar_tela_inicial(self):
        self.janela.deiconify()

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
