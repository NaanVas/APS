import tkinter as tk
from tkinter import ttk
from visao.tela.tela_padrao import TelaPadrao
from controle.emprestimo_controller import EmprestimoController

class TelaListarEmprestimos(TelaPadrao):
    def __init__(self, root, cpf):
        super().__init__(root, "Listagem de Empréstimos")
        self.janela.focus_set()
        self.emprestimo_controller = EmprestimoController()
        self.text_area = None
        self.cpf = cpf

        self.janela.geometry("600x450+800+150")

        self.configurar_interface()

    def configurar_interface(self):
        self.janela_listar_aberta = True
        label_titulo = tk.Label(self.frame_central, text="Listagem de Empréstimos", font=("Montserrat", 18, "bold"), fg="#893F04", bg="#E5E0D8")
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

    def listar_emprestimos(self):
        return self.emprestimo_controller.listar_emprestimos()

    def atualizar_lista(self):
        if self.janela_listar_aberta and self.text_area:
            self.text_area.delete('1.0', tk.END) 
            emprestimos = []

            if self.cpf == None:
                emprestimos = self.listar_emprestimos()
            
            else:
                todos_emprestimos = self.listar_emprestimos()
                for emprestimo in todos_emprestimos:
                    if emprestimo.get_cpf_usuario() == self.cpf:
                        emprestimos.append(emprestimo)

            for emprestimo in emprestimos:
                cpf_funcionario = f"CPF Funcionário: {emprestimo.get_cpf_funcionario()}\n"
                cpf_usuario = f"CPF Usuário: {emprestimo.get_cpf_usuario()}\n"
                livros = f"Livros: {', '.join(emprestimo.get_livros())}\n"
                data_emprestimo = f"Data de Empréstimo: {emprestimo.get_data_emprestimo().strftime('%Y-%m-%d %H:%M:%S') if emprestimo.get_data_emprestimo() else 'N/A'}\n"
                data_devolucao = f"Data de Devolução: {emprestimo.get_data_devolucao().strftime('%Y-%m-%d') if emprestimo.get_data_devolucao() else 'N/A'}\n"
                status = f"Status: {emprestimo.get_status()}\n"

                self.text_area.insert(tk.END, cpf_funcionario)
                self.text_area.insert(tk.END, cpf_usuario)
                self.text_area.insert(tk.END, livros)
                self.text_area.insert(tk.END, data_emprestimo)
                self.text_area.insert(tk.END, data_devolucao)
                self.text_area.insert(tk.END, status)
                self.text_area.insert(tk.END, "\n")

                self.text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))
