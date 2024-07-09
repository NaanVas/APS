import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from controle.autor_controller import AutorController

class TelaBuscarAutor(TelaPadrao):
    def __init__(self, root, voltar_callback):
        super().__init__(root, "Buscar Autor")
        self.voltar_callback = voltar_callback
        self.autor_controller = AutorController()

        label_titulo = tk.Label(self.frame_central, text="Buscar Autor", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(self.frame_central, text="Nome:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_buscar_nome = tk.Entry(self.frame_central)
        self.entry_buscar_nome.grid(row=1, column=1, pady=5)

        self.label_mensagem = tk.Label(self.frame_central, text="", font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.grid(row=2, column=0, columnspan=2, pady=10)

        botao_buscar = ttk.Button(self.frame_central, text="Buscar", style="Estilo.TButton", command=self.buscar_autor)
        botao_buscar.grid(row=3, column=0, pady=10)

        botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela)
        botao_voltar.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela)

    def fechar_tela(self):
        self.janela.destroy()
        self.voltar_callback()
    
    def buscar_autor(self):
        nome = self.entry_buscar_nome.get()
        if nome:
            autor = self.autor_controller.buscar_autor(nome)
            if autor:
                self.exibir_resultado_busca(autor)
            else:
                self.exibir_mensagem_erro(f"Autor '{nome}' não encontrado.")
        else:
            self.exibir_mensagem_erro("Digite o nome do autor.")

    def exibir_resultado_busca(self, autor):
        resultado = f"Nome: {autor.get_nome()}\n" \
                    f"Nacionalidade: {autor.get_nacionalidade()}\n" \
                    f"Data de Nascimento: {autor.get_data_nascimento()}"

        self.label_mensagem.config(text=resultado, fg="black")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")
