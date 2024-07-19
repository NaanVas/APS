import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.funcionario_controller import FuncionarioController

class TelaBuscarFuncionario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Buscar Funcionário")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.funcionario_controller = FuncionarioController()

        label_titulo = tk.Label(self.frame_central, text="Buscar Funcionário", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        self.botao_buscar = ttk.Button(self.frame_central, text="Buscar", style="Estilo.TButton", command=self.buscar_funcionario)
        self.botao_buscar.grid(row=3, column=0, pady=10)

        self.botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        self.botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def buscar_funcionario(self):
        cpf = self.entry_cpf.get()

        if not cpf:
            self.label_mensagem.config(text="Digite o CPF para buscar.")
            return

        funcionario = self.funcionario_controller.buscar_funcionario(cpf)
        if funcionario:
            self.mostrar_dados_funcionario(funcionario)
        else:
            self.label_mensagem.config(text=f"Funcionário com CPF '{cpf}' não encontrado.")

    def mostrar_dados_funcionario(self, funcionario):
        self.label_mensagem.config(text="")
        info_funcionario = f"CPF: {funcionario.get_cpf()}\nNome: {funcionario.get_nome()}\nData de Nascimento: {funcionario.get_data_nascimento()}"
        tk.Label(self.frame_central, text=info_funcionario, font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, columnspan=2, pady=10)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
