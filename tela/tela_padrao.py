import tkinter as tk
from tkinter import ttk

class TelaPadrao:
    def __init__(self, root, titulo):
        self.root = root
        self.titulo = titulo

        self.janela = tk.Toplevel(self.root)
        self.janela.title(self.titulo)
        self.janela.geometry("600x450+150+150")
        self.janela.configure(bg="#F0DAAE")
        self.janela.focus_set()

        self.frame_central = tk.Frame(self.janela, bg="#F0DAAE")
        self.frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Configuração do estilo para os botões
        self.estilo_botoes = ttk.Style()
        self.estilo_botoes.configure("Estilo.TButton", font=("Montserrat", 10), foreground="#482E1D", background="#482E1D", borderwidth=0)
        self.estilo_botoes.map("Estilo.TButton", background=[("active", "#482E1D")])