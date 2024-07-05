import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.usuario_controller import UsuarioController

class TelaBuscarUsuario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Buscar Usuário")
        self.voltar_callback = voltar_callback
        self.usuario_controller = UsuarioController()

        label_titulo = tk.Label(self.frame_central, text="Buscar Usuário", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_cpf = tk.Entry(self.frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 10), fg="red", bg="#F0DAAE")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_buscar = ttk.Button(self.frame_central, text="Buscar", style="Estilo.TButton", command=self.buscar_usuario)
        botao_buscar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def buscar_usuario(self):
        cpf = self.entry_cpf.get()
        if cpf:
            usuario = self.usuario_controller.buscar_usuario(cpf)
            if usuario:
                self.exibir_resultado_busca(usuario)
            else:
                self.exibir_mensagem_erro(f"Usuário com CPF '{cpf}' não encontrado.")
        else:
            self.exibir_mensagem_erro("Digite o CPF do usuário.")

    def exibir_resultado_busca(self, usuario):
        resultado = f"CPF: {usuario.get_cpf()}\n" \
                    f"Nome: {usuario.get_nome()}\n" \
                    f"Tipo: {usuario.get_tipo()}\n" \
                    f"Salário: {usuario.get_salario()}"  # Ajuste conforme os atributos do usuário

        self.label_mensagem.config(text=resultado, fg="black")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
