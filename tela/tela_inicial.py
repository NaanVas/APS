import tkinter as tk
from tkinter import ttk
from tela.tela_padrao import TelaPadrao
from tela.livro.livro import TelaInicialLivro
#from tela.autor import TelaAutor
from tela.usuario.usuario import TelaInicialUsuario

class TelaInicial:
    def __init__(self, root):
        self.root = root

        self.janela = tk.Toplevel(self.root)
        self.janela.title("Sistema de Gerenciamento de Biblioteca")
        self.janela.geometry("600x450+150+150")
        self.janela.configure(bg="#F0DAAE")
        self.janela.focus_set()

        self.frame_central = tk.Frame(self.janela, bg="#F0DAAE")
        self.frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Rótulo de boas-vindas
        self.label_boas_vindas = tk.Label(self.root, text="Bem-vindo ao Sistema de Biblioteca", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        self.label_boas_vindas.pack(pady=20)

        # Rótulo de boas-vindas
        self.label_boas_vindas = tk.Label(self.frame_central, text="Bem-vindo ao Sistema de Biblioteca", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        self.label_boas_vindas.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame para os botões
        self.frame_botoes = tk.Frame(self.frame_central, bg="#F0DAAE")
        self.frame_botoes.grid(row=1, column=0, columnspan=2, pady=20)

        # Estilo para os botões
        self.estilo_botoes = ttk.Style()
        self.estilo_botoes.configure("Estilo.TButton", font=("Montserrat", 10), foreground="#482E1D", background="#482E1D", borderwidth=0)
        self.estilo_botoes.map("Estilo.TButton", background=[("active", "#482E1D")])

        self.botao_livro = ttk.Button(self.frame_botoes, text="Livro", style="Estilo.TButton", command=self.abrir_tela_livro)
        self.botao_livro.grid(row=0, column=0, pady=10, padx=10, sticky="ew")

        self.botao_autor = ttk.Button(self.frame_botoes, text="Autor", style="Estilo.TButton", command=self.abrir_tela_autor)
        self.botao_autor.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        self.botao_emprestimo = ttk.Button(self.frame_botoes, text="Empréstimo", style="Estilo.TButton", command=self.abrir_tela_emprestimo)
        self.botao_emprestimo.grid(row=2, column=0, pady=10, padx=10, sticky="ew")

        self.botao_devolucoes = ttk.Button(self.frame_botoes, text="Devoluções", style="Estilo.TButton", command=self.abrir_tela_devolucoes)
        self.botao_devolucoes.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        self.botao_usuario = ttk.Button(self.frame_botoes, text="Usuário", style="Estilo.TButton", command=self.abrir_tela_usuario)
        self.botao_usuario.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

        #botao_voltar = ttk.Button(self.frame_central, text="Voltar", style="Estilo.TButton", command=self.fechar_tela_inicial)
        #botao_voltar.grid(row=5, column=0, pady=10, padx=10, sticky="ew")

        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_tela_inicial)

    def abrir_tela_livro(self):
        self.janela.withdraw()
        self.janela_livro = TelaInicialLivro(self.root, self.voltar_tela_inicial)

    def abrir_tela_autor(self):
        self.janela.withdraw()
        # TelaAutor(self.root, self.voltar_tela_inicial)
        pass

    def abrir_tela_emprestimo(self):
        # Implementar a lógica para abrir a tela de empréstimo
        pass

    def abrir_tela_devolucoes(self):
        # Implementar a lógica para abrir a tela de devoluções
        pass

    def abrir_tela_usuario(self):
        self.janela.withdraw()
        self.janela_usuario = TelaInicialUsuario(self.root, self.voltar_tela_inicial)

    def voltar_tela_inicial(self):
        self.janela.deiconify()
    
    def fechar_tela_inicial(self):
        self.janela.destroy()
        self.root.destroy()
