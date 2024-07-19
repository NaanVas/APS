import tkinter as tk
from visao.tela.tela_padrao import TelaPadrao
from controle.funcionario_controller import FuncionarioController

class TelaListarFuncionarios(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Listagem de Funcionários")
        self.janela.focus_set()
        self.voltar_callback = voltar_callback
        self.funcionario_controller = FuncionarioController()
        self.text_area = None  

        self.janela.geometry("600x450+800+150")

        self.configurar_interface()

    def configurar_interface(self):
        self.janela_listar_aberta = True

        label_titulo = tk.Label(self.frame_central, text="Listagem de Funcionários", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        scrollbar = tk.Scrollbar(self.janela)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(self.janela, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#E5E0D8", font=("Montserrat", 10))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.text_area.yview)

        self.atualizar_lista()

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela_listar_aberta = False
        self.janela.destroy()
        self.voltar_callback()

    def listar_funcionarios(self):
        return self.funcionario_controller.listar_funcionarios()

    def atualizar_lista(self):
        if self.janela_listar_aberta and self.text_area:
            self.text_area.delete('1.0', tk.END)

            funcionarios = self.listar_funcionarios()

            for funcionario in funcionarios:
                cpf = f"CPF: {funcionario.get_cpf()}\n"
                nome = f"Nome: {funcionario.get_nome()}\n"
                data_nascimento = f"Data de Nascimento: {funcionario.get_data_nascimento()}\n"
                
                self.text_area.insert(tk.END, cpf, "negrito")
                self.text_area.insert(tk.END, nome)
                self.text_area.insert(tk.END, data_nascimento)
                self.text_area.insert(tk.END, "\n")

                self.text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))
