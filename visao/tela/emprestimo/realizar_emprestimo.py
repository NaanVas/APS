import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from visao.tela.emprestimo.emprestimo_iniciado import TelaEmprestimoIniciado
from controle.emprestimo_controller import EmprestimoController

class TelaRealizarEmprestimo(TelaPadrao):
    def __init__(self, root, voltar_callback, cpf):
        super().__init__(root, "Empréstimo")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.cpf = cpf
        self.emprestimo_controller = EmprestimoController()

        label_titulo = tk.Label(self.frame_central, text="Empréstimo de Livro", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="CPF do Usuário:", font=("Montserrat", 10), fg="#893F04", bg="#E5E0D8").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_cpf_usuario = tk.Entry(self.frame_central)
        self.entry_cpf_usuario.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#893F04", bg="#E5E0D8")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_realizar = ttk.Button(self.frame_central, text="Realizar Empréstimo", style="Estilo.TButton", command=self.realizar_emprestimo)
        botao_realizar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()

    def realizar_emprestimo(self):
        cpf_usuario = self.entry_cpf_usuario.get()
        if cpf_usuario: 
                emprestimo = self.emprestimo_controller.iniciar_emprestimo(self.cpf, cpf_usuario)
                if isinstance(emprestimo, str):
                    self.exibir_mensagem_erro(emprestimo)
                else:
                    resultado = self.emprestimo_controller.buscar_data_pendente(cpf_usuario)
                    if resultado == None:
                        self.janela.withdraw()
                        self.entry_cpf_usuario.delete(0, tk.END)
                        self.janela_emprestimo  = TelaEmprestimoIniciado(self.root, self.voltar_para_tela_emprestimo, self.cpf, cpf_usuario, emprestimo)
                    else:
                        self.exibir_mensagem_erro(resultado)

        else:
            self.exibir_mensagem_erro("Preencha todos os campos.")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def voltar_para_tela_emprestimo(self):
        self.janela.deiconify()
