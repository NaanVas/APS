import tkinter as tk
from tkinter import ttk
from tela.tela_inicial import TelaInicial

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.abrir_tela_inicial()
        '''
        self.frame = tk.Frame(self.root, bg="#F0DAAE")
        self.frame.pack(expand=True, fill="both")

        self.botao_login = ttk.Button(self.frame, text="Login", style="Estilo.TButton", command=self.abrir_tela_inicial)
        self.botao_login.pack(pady=20)
        '''
    def abrir_tela_inicial(self):
        self.root.withdraw()
        self.tela_inicial = TelaInicial(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    root.mainloop()
