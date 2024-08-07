import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.emprestimo.listar_livros_emprestimo import TelaListarLivrosEmprestimo
from controle.emprestimo_controller import EmprestimoController

class TelaEmprestimoIniciado(TelaPadrao):
    def __init__(self, root, voltar_callback, cpf_funcionario, cpf_usuario, emprestimo):
        super().__init__(root, "Empréstimo Iniciado")
        self.janela.focus_set()
        self.emprestimo = emprestimo
        self.voltar_callback = voltar_callback
        self.emprestimo_controller = EmprestimoController()
        self.janela_listar_aberta = None
        self.cpf_funcionario = cpf_funcionario
        self.cpf_usuario = cpf_usuario

        label_titulo = tk.Label(self.frame_central, text="Empréstimo de Livro", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Título do Livro:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_titulo_livro = tk.Entry(self.frame_central)
        self.entry_titulo_livro.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_adicionar = ttk.Button(self.frame_central, text="Adicionar Livro", style="Estilo.TButton", command=self.adicionar_livro)
        botao_adicionar.grid(row=3, column=0, pady=10)

        botao_remover = ttk.Button(self.frame_central, text="Remover Livro", style="Estilo.TButton", command=self.remover_livro)
        botao_remover.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        botao_listar = ttk.Button(self.frame_central, text="Listar Livros", style="Estilo.TButton", command=self.listar_livros)
        botao_listar.grid(row=4, column=0, pady=10)

        botao_aprovar = ttk.Button(self.frame_central, text="Aprovar Empréstimo", style="Estilo.TButton", command=self.aprovar_emprestimo)
        botao_aprovar.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        botao_cancelar = ttk.Button(self.frame_central, text="Cancelar Empréstimo", style="Estilo.TButton", command=self.fechar_tela)
        botao_cancelar.grid(row=5, column=0, columnspan=2, pady=10)

    def adicionar_livro(self):
        titulo = self.entry_titulo_livro.get()
        if titulo:
                resultado = self.emprestimo_controller.adicionar_livro(self.emprestimo, titulo)
                if resultado == None:
                    self.exibir_mensagem_sucesso(f"Livro '{titulo}' adicionado.")
                    self.entry_titulo_livro.delete(0, tk.END)
                else:
                    self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o título do livro.")

    def remover_livro(self):
        titulo = self.entry_titulo_livro.get()
        if titulo:
                resultado = self.emprestimo_controller.remover_livro(self.emprestimo, titulo)
                if resultado == None:
                    self.exibir_mensagem_sucesso(f"Livro '{titulo}' removido.")
                    self.entry_titulo_livro.delete(0, tk.END)

                else:
                    self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o título do livro.")

    def listar_livros(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarLivrosEmprestimo(self.root, self.emprestimo.livros)

    def aprovar_emprestimo(self):
            resultado = self.emprestimo_controller.aprovar_emprestimo(self.emprestimo)
            if resultado == None:
                self.exibir_mensagem_sucesso("Empréstimo aprovado.")
                self.fechar_tela()
            else:
                self.exibir_mensagem_erro(resultado)

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()
