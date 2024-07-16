import tkinter as tk
from tkinter import ttk
from visao.tela.tela_login import TelaLogin

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.root.title("Sistema de Gestão")
        self.tela_login = TelaLogin(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
