import tkinter as tk
from tkinter import ttk
from visao.tela.emprestimo.realizar_emprestimo import TelaRealizarEmprestimo
from visao.tela.emprestimo.realizar_devolução import TelaRealizarDevolucao
from visao.tela.emprestimo.verifica_emprestimo import TelaVerificarEmprestimo
from visao.tela.emprestimo.listar_emprestimos import TelaListarEmprestimos
from visao.tela.tela_padrao import TelaPadrao

class TelaEmprestimoMenu(TelaPadrao):
    def __init__(self, root, voltar_callback, cpf):
        super().__init__(root, "Menu de Empréstimo")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.cpf = cpf
        self.janela_listar_aberta = None


        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)

        label_titulo = tk.Label(self.frame_central, text="Menu Empréstimo", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.botao_realizar_emprestimo = ttk.Button(self.frame_botoes, text="Realizar Empréstimo", style="Estilo.TButton", command=self.realizar_emprestimo)
        self.botao_realizar_emprestimo.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        self.botao_verificar_emprestimo = ttk.Button(self.frame_botoes, text="Verificar Empréstimo", style="Estilo.TButton", command=self.verificar_emprestimo)
        self.botao_verificar_emprestimo.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        self.botao_listar_emprestimos = ttk.Button(self.frame_botoes, text="Listar Empréstimos", style="Estilo.TButton", command=self.listar_emprestimos)
        self.botao_listar_emprestimos.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        self.bota_realizar_devolucao = ttk.Button(self.frame_botoes, text="Realizar Devolução", style="Estilo.TButton", command=self.realizar_devolução)
        self.bota_realizar_devolucao.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        botao_voltar = ttk.Button(self.frame_botoes, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=5, column=0, pady=10, columnspan=2, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def realizar_emprestimo(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.withdraw()
        self.janela_emprestimo = TelaRealizarEmprestimo(self.root, self.voltar_para_tela_emprestimo_menu, self.cpf)

    def verificar_emprestimo(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.withdraw()
        self.janela_verifica_emprestimo = TelaVerificarEmprestimo(self.root, self.voltar_para_tela_emprestimo_menu)

    def listar_emprestimos(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela_listar_aberta = TelaListarEmprestimos(self.root, None)

    def realizar_devolução(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.withdraw()
        self.janela_listar_aberta = TelaRealizarDevolucao(self.root, self.voltar_para_tela_emprestimo_menu,self.cpf)

    def voltar_para_tela_emprestimo_menu(self):
        self.janela.deiconify()

    def fechar_tela(self):
        if self.janela_listar_aberta:
            self.janela_listar_aberta.fechar_tela()
        self.janela.destroy()
        self.voltar_callback()
