import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.emprestimo_controller import EmprestimoController

class TelaRealizarDevolucao(TelaPadrao):
    def __init__(self, root, voltar_callback, cpf_funcionario):
        super().__init__(root, "Devolução de Livro")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.cpf_funcionario = cpf_funcionario
        self.emprestimo_controller = EmprestimoController()

        label_titulo = tk.Label(self.frame_central, text="Devolução de Livro", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF do Usuário:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_cpf_usuario = tk.Entry(self.frame_central)
        self.entry_cpf_usuario.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_central, text="Título do Livro:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=2, column=0, pady=5, sticky='e', padx=15)
        self.entry_titulo_livro = tk.Entry(self.frame_central)
        self.entry_titulo_livro.grid(row=2, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=3, column=0, columnspan=2, pady=10)

        botao_realizar_devolucao = ttk.Button(self.frame_central, text="Realizar Devolução", style="Estilo.TButton", command=self.realizar_devolucao)
        botao_realizar_devolucao.grid(row=4, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def realizar_devolucao(self):
        cpf_usuario = self.entry_cpf_usuario.get()
        titulo_livro = self.entry_titulo_livro.get()

        if cpf_usuario and titulo_livro:
            resultado = self.emprestimo_controller.realizar_devolucao(cpf_usuario, titulo_livro)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Devolução do livro '{titulo_livro}' realizada com sucesso.")
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Preencha todos os campos.")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")
        self.entry_cpf_usuario.delete(0, tk.END)
        self.entry_titulo_livro.delete(0, tk.END)
