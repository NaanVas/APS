import tkinter as tk
from tkinter import ttk
from tela_livro import TelaLivro
from tela_autor import TelaAutor
from tela_usuario import TelaUsuario

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Biblioteca")
        self.root.geometry("600x450")
        self.root.configure(bg="#F0DAAE")

        largura = 600
        altura = 450
        pos_x = 150  
        pos_y = 150 
        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.root.focus_set()

        # Rótulo de boas-vindas
        self.label_boas_vindas = tk.Label(self.root, text="Bem-vindo ao Sistema de Biblioteca", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        self.label_boas_vindas.pack(pady=20)

        # Frame para os botões
        self.frame_botoes = tk.Frame(self.root, bg="#F0DAAE") 
        self.frame_botoes.pack()

        # Estilo para os botões
        self.estilo_botoes = ttk.Style()
        self.estilo_botoes.configure("Estilo.TButton", font=("Montserrat", 10), foreground="#482E1D", background="#482E1D", borderwidth=0)
        self.estilo_botoes.map("Estilo.TButton", background=[("active", "#482E1D")])

        self.botao_livro = ttk.Button(self.frame_botoes, text="Livro", style="Estilo.TButton", command=self.abrir_tela_livro)
        self.botao_livro.pack(pady=10)

        self.botao_autor = ttk.Button(self.frame_botoes, text="Autor", style="Estilo.TButton", command=self.abrir_tela_autor)
        self.botao_autor.pack(pady=10)

        self.botao_emprestimo = ttk.Button(self.frame_botoes, text="Empréstimo", style="Estilo.TButton", command=self.abrir_tela_emprestimo)
        self.botao_emprestimo.pack(pady=10)

        self.botao_devolucoes = ttk.Button(self.frame_botoes, text="Devoluções", style="Estilo.TButton", command=self.abrir_tela_devolucoes)
        self.botao_devolucoes.pack(pady=10)

        self.botao_usuario = ttk.Button(self.frame_botoes, text="Usuário", style="Estilo.TButton", command=self.abrir_tela_usuario)
        self.botao_usuario.pack(pady=10)


    def abrir_tela_livro(self):
        self.root.withdraw()
        self.janela_livro = TelaLivro(self.root, self.voltar_tela_inicial)
        

    def voltar_tela_inicial(self):
        self.root.deiconify()
        
    def abrir_tela_autor(self):
        self.root.withdraw()
        self.jenela_autor = TelaAutor(self.root, self.voltar_tela_inicial)

    def abrir_tela_emprestimo(self):
        pass
        
    def abrir_tela_devolucoes(self):
        pass
        
    def abrir_tela_usuario(self):
        self.root.withdraw()
        self.janela_usuario = TelaUsuario(self.root, self.voltar_tela_inicial)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()