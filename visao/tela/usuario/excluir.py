import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.usuario_controller import UsuarioController

class TelaExcluirUsuario(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Excluir Usuário")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.usuario_controller = UsuarioController()

        label_titulo = tk.Label(self.frame_central, text="Excluir Usuário", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_excluir_cpf = tk.Entry(self.frame_central)
        self.entry_excluir_cpf.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        self.botao_salvar = ttk.Button(self.frame_central, text="Excluir", style="Estilo.TButton", command=self.excluir_usuario)
        self.botao_salvar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
    
    def excluir_usuario(self):
        cpf = self.entry_excluir_cpf.get()
        if cpf:
            resultado = self.usuario_controller.excluir_usuario(cpf)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Usuário com CPF '{cpf}' excluído com sucesso.")
                self.limpar_campos()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o CPF do usuário a ser excluído.")

    def limpar_campos(self):
        self.entry_excluir_cpf.delete(0, tk.END)
        self.entry_excluir_cpf.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
