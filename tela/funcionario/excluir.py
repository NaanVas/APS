import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.funcionario_controller import FuncionarioController

class TelaExcluirFuncionario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Excluir Funcionário")
        self.voltar_callback = voltar_callback
        self.funcionario_controller = FuncionarioController()

        label_titulo = tk.Label(self.frame_central, text="Excluir Funcionário", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        self.botao_excluir = ttk.Button(self.frame_central, text="Excluir", style="Estilo.TButton", command=self.excluir_funcionario)
        self.botao_excluir.grid(row=3, column=0, pady=10)

        self.botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        self.botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def excluir_funcionario(self):
        cpf = self.entry_cpf.get()

        if not cpf:
            self.label_mensagem.config(text="Digite o CPF para excluir.")
            return

        resultado = self.funcionario_controller.excluir_funcionario(cpf)
        if resultado:
            self.label_mensagem.config(text=f"Funcionário com CPF '{cpf}' excluído com sucesso.")
        else:
            self.label_mensagem.config(text=f"Erro ao excluir funcionário com CPF '{cpf}'.")

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
