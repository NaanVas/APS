import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.usuario_controller import UsuarioController
from modelo.funcionario import Funcionario

class TelaListarUsuarios(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Listagem de Usuários")
        self.voltar_callback = voltar_callback
        self.usuario_controller = UsuarioController()
        self.text_area = None  

        self.configurar_interface()

    def configurar_interface(self):
        self.janela_listar_aberta = True

        label_titulo = tk.Label(self.frame_central, text="Listagem de Usuários", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        scrollbar = tk.Scrollbar(self.janela)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(self.janela, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#F0DAAE", font=("Montserrat", 10))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.text_area.yview)

        self.atualizar_lista()

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)


    def fechar_tela(self):
        self.janela_listar_aberta = False
        self.janela.destroy()
        self.voltar_callback()

    def listar_usuarios(self):
        return self.usuario_controller.listar_usuarios()

    def atualizar_lista(self):
         if self.janela_listar_aberta and self.text_area:
            self.text_area.delete('1.0', tk.END)  # Limpar o conteúdo atual

            usuarios = self.listar_usuarios()

            for usuario in usuarios:
                cpf = f"CPF: {usuario.get_cpf()}\n"
                nome = f"Nome: {usuario.get_nome()}\n"
                tipo = f"Tipo: {usuario.get_tipo()}\n"
            
                # Inserir texto formatado com tags de estilo no tkinter
                self.text_area.insert(tk.END, cpf, "negrito")
                self.text_area.insert(tk.END, nome)
                self.text_area.insert(tk.END, tipo)

                self.text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))


    # Sobrescrevendo o método voltar para utilizar o callback específico
    def voltar(self):
        self.janela.destroy()
        self.voltar_callback()