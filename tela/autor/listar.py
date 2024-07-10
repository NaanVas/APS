import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.autor_controller import AutorController

class TelaListarAutores(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Listagem de Autores")
        self.voltar_callback = voltar_callback
        self.autor_controller = AutorController()
        self.text_area = None  
        self.scrollbar = None

        self.configurar_interface()

    def configurar_interface(self):
        self.janela_listar_aberta = True

        label_titulo = tk.Label(self.frame_central, text="Listagem de Autores", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.scrollbar = ttk.Scrollbar(self.frame_central, orient=tk.VERTICAL)
        self.scrollbar.grid(row=1, column=2, sticky='ns')

        self.text_area = tk.Text(self.frame_central, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, bg="#F0DAAE", font=("Montserrat", 10))
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.scrollbar.config(command=self.text_area.yview)

        self.atualizar_lista()

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=2, column=0, columnspan=2, pady=10)

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela_listar_aberta = False
        self.janela.destroy()
        self.voltar_callback()

    def listar_autores(self):
        return self.autor_controller.listar_autores()

    def atualizar_lista(self):
        if self.janela_listar_aberta and self.text_area:
            self.text_area.delete('1.0', tk.END)

            autores = self.listar_autores()

            for autor in autores:
                nome = f"Nome: {autor.get_nome()}\n"
                nacionalidade = f"Nacionalidade: {autor.get_nacionalidade()}\n"
                data_nascimento = f"Data de Nascimento: {autor.get_data_nascimento()}\n"
                
                self.text_area.insert(tk.END, nome, "negrito")
                self.text_area.insert(tk.END, nacionalidade)
                self.text_area.insert(tk.END, data_nascimento)
                self.text_area.insert(tk.END, "\n")

            self.text_area.configure(state='disabled')
