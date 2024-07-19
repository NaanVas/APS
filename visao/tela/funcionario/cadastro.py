import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.funcionario_controller import FuncionarioController

class TelaCadastroFuncionario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Cadastro de Funcionário")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.funcionario_controller = FuncionarioController()

        label_titulo = tk.Label(self.frame_central, text="Cadastrar Funcionário", font=("Montserrat", 16, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        tk.Label(self.frame_central, text="Nome:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=2, column=0, pady=5, sticky='e')
        self.entry_nome = tk.Entry(self.frame_central)
        self.entry_nome.grid(row=2, column=1, pady=5)

        tk.Label(self.frame_central, text="Data de Nascimento:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=3, column=0, pady=5, sticky='e')
        self.entry_data_nascimento = tk.Entry(self.frame_central)
        self.entry_data_nascimento.grid(row=3, column=1, pady=5)

        tk.Label(self.frame_central, text="Salário:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=4, column=0, pady=5, sticky='e')
        self.entry_salario = tk.Entry(self.frame_central)
        self.entry_salario.grid(row=4, column=1, pady=5)

        tk.Label(self.frame_central, text="Senha:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=5, column=0, pady=5, sticky='e')
        self.entry_senha = tk.Entry(self.frame_central, show="*")
        self.entry_senha.grid(row=5, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=6, column=0, columnspan=2, pady=10)

        self.botao_salvar = ttk.Button(self.frame_central, text="Salvar", style="Estilo.TButton", command=self.cadastrar_funcionario)
        self.botao_salvar.grid(row=7, column=0, pady=10)

        self.botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        self.botao_voltar.grid(row=7, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def cadastrar_funcionario(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        salario = self.entry_salario.get()
        senha = self.entry_senha.get()

        if not cpf or not nome or not data_nascimento or not salario or not senha:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")
            return

        try:
            salario = float(salario)
        except ValueError:
            self.exibir_mensagem_erro("O campo Salário deve ser numérico.")
            return

        resultado = self.funcionario_controller.cadastrar_funcionario(cpf, nome, data_nascimento, salario, senha)
        if resultado is None:
            self.exibir_mensagem_sucesso("Funcionário cadastrado com sucesso.")
            self.limpar_campos()
        else:
            self.exibir_mensagem_erro("Erro ao cadastrar funcionário.")

    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_salario.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_cpf.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
