import tkinter as tk
from tkinter import ttk
from controle.autor_controller import AutorController

class TelaAutor:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback
        self.autor_c = AutorController()
        self.janela_listar_aberta = False

        self.janela_autor = tk.Toplevel(self.root)
        self.janela_autor.title("Gerenciamento de Autores")
        self.janela_autor.geometry("450x300")
        self.janela_autor.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150 
        pos_y = 150 
        self.janela_autor.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_autor.focus_set()

        label_titulo = tk.Label(self.janela_autor, text="Tela de Gerenciamento de Autores", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        botao_cadastrar = ttk.Button(self.janela_autor, text="Cadastrar Autor", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.pack(pady=10)

        botao_buscar = ttk.Button(self.janela_autor, text="Buscar Autor", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.pack(pady=10)

        botao_excluir = ttk.Button(self.janela_autor, text="Excluir Autor", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.pack(pady=10)

        botao_listar = ttk.Button(self.janela_autor, text="Listar Autores", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_autor, text="Voltar", style="Estilo.TButton", command=self.fechar_tela_autor)
        botao_voltar.pack(pady=10)

        self.janela_autor.protocol("WM_DELETE_WINDOW", self.fechar_tela_autor)
    
    def fechar_tela_autor(self):
        self.janela_autor.destroy()
        self.voltar_callback()
    
    def abrir_tela_cadastrar(self):
        self.janela_autor.withdraw()

        self.janela_cadastrar = tk.Toplevel(self.janela_autor)
        self.janela_cadastrar.title("Cadastrar Autor")
        self.janela_cadastrar.geometry("300x470")
        self.janela_cadastrar.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
        self.janela_cadastrar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_cadastrar.focus_set()

        label_titulo = tk.Label(self.janela_cadastrar, text="Cadastrar Autor", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        tk.Label(self.janela_cadastrar, text="Nome:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_nome = tk.Entry(self.janela_cadastrar)
        self.entry_nome.pack(pady=5)

        tk.Label(self.janela_cadastrar, text="Nacionalidade:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_nacionalidade = tk.Entry(self.janela_cadastrar)
        self.entry_nacionalidade.pack(pady=5)

        tk.Label(self.janela_cadastrar, text="Data de Nascimento:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_data_nascimento = tk.Entry(self.janela_cadastrar)
        self.entry_data_nascimento.pack(pady=5)

        self.label_mensagem = tk.Label(self.janela_cadastrar, text="",font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_salvar = ttk.Button(self.janela_cadastrar, text="Salvar", style="Estilo.TButton", command=self.salvar_autor)
        botao_salvar.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_cadastrar, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_autor(self.janela_cadastrar))
        botao_voltar.pack(pady=10)

        self.janela_cadastrar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_autor(self.janela_cadastrar))

    def salvar_autor(self):
        nome = self.entry_nome.get()
        nacionalidade = self.entry_nacionalidade.get()
        data_nascimento = self.entry_data_nascimento.get()
        
        if nome and nacionalidade and data_nascimento:
            resultado = self.autor_c.cadastrar_autor(nome, nacionalidade, data_nascimento)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Autor '{nome}' cadastrado com sucesso.")
                self.limpar_campos()

                if self.janela_listar_aberta:
                    self.abrir_tela_listar()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_nacionalidade.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_nome.focus_set()

    def abrir_tela_excluir(self):
        self.janela_autor.withdraw()

        self.janela_excluir = tk.Toplevel(self.root)
        self.janela_excluir.title("Excluir Autor")
        self.janela_excluir.geometry("400x300")
        self.janela_excluir.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
    
        self.janela_excluir.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_excluir.focus_set()

        label_titulo = tk.Label(self.janela_excluir, text="Excluir Autor", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        entry_nome = tk.Entry(self.janela_excluir)
        entry_nome.pack(pady=10)

        self.label_mensagem = tk.Label(self.janela_excluir, text="",font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_excluir = ttk.Button(self.janela_excluir, text="Excluir", style="Estilo.TButton", command=lambda: self.excluir_autor(entry_nome.get()))
        botao_excluir.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_excluir, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_autor(self.janela_excluir))
        botao_voltar.pack(pady=10)

        self.janela_excluir.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_autor(self.janela_excluir))

    def excluir_autor(self, nome):
        resultado = self.autor_c.excluir_autor(nome)
        if resultado is None:
            self.exibir_mensagem_sucesso(f"Autor '{nome}' excluído com sucesso.")

            if self.janela_listar_aberta:
                self.abrir_tela_listar()
        else:
            self.exibir_mensagem_erro(resultado)

    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar.destroy()
        self.janela_listar_aberta = True
        autores = self.autor_c.listar_autores()

        self.janela_listar = tk.Toplevel(self.root)
        self.janela_listar.title("Listagem de Autores")
        self.janela_listar.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        largura_tela = self.janela_listar.winfo_screenwidth()
        pos_x = largura_tela - largura - 150 
        pos_y = 150 
        self.janela_listar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_listar.focus_set()

        # Configurar scrollbar
        scrollbar = tk.Scrollbar(self.janela_listar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget para exibir os autores com scrollbar
        text_area = tk.Text(self.janela_listar, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#F0DAAE", font=("Montserrat", 10))
        text_area.pack(fill=tk.BOTH, expand=True)

        # Configurar a scrollbar para interagir com o widget de texto
        scrollbar.config(command=text_area.yview)

        # Escrever os autores no widget de texto
        for autor in autores:
            nome = f"Nome: {autor.get_nome()}\n"
            nacionalidade = f"Nacionalidade: {autor.get_nacionalidade()}\n"
            nascimento = f"Data de Nascimento: {autor.get_data_nascimento()}\n\n"

            # Inserir texto formatado com tags de estilo no tkinter
            text_area.insert(tk.END, nome, "negrito")
            text_area.insert(tk.END, nacionalidade)
            text_area.insert(tk.END, nascimento)

            text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))

        self.janela_listar.protocol("WM_DELETE_WINDOW", self.fechar_janela_listar)

    def fechar_janela_listar(self):
        self.janela_listar_aberta = False
        self.janela_listar.destroy()

    def abrir_tela_buscar(self):
        self.janela_buscar = tk.Toplevel(self.janela_autor)
        self.janela_buscar.title("Buscar Livro")
        self.janela_buscar.geometry("400x200")
        self.janela_buscar.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
        self.janela_buscar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_buscar.focus_set()

        label_nome = tk.Label(self.janela_buscar, text="Buscar Autor", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_nome.pack(pady=20)

        tk.Label(self.janela_buscar, text="Nome:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_busca_nome = tk.Entry(self.janela_buscar)
        self.entry_busca_nome.pack(pady=5)

        botao_buscar = ttk.Button(self.janela_buscar, text="Buscar", style="Estilo.TButton", command=self.buscar_autor)
        botao_buscar.pack(pady=10)

        self.label_mensagem = tk.Label(self.janela_buscar, text="", font=("Montserrat", 10), fg="red", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_buscar, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_autor(self.janela_buscar))
        botao_voltar.pack(pady=10)

        self.janela_buscar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_autor(self.janela_buscar))

    def buscar_autor(self):
        nome = self.entry_busca_nome.get()
        if nome:
            autor = self.autor_c.buscar_autor(nome)
            if autor:
                self.exibir_resultado_busca(autor)
                self.entry_busca_nome.delete(0, tk.END)
                self.entry_busca_nome.focus_set()

            else:
                self.exibir_mensagem_erro(f"Autor '{nome}' não encontrado.")
                self.entry_busca_nome.delete(0, tk.END)
                self.entry_busca_nome.focus_set()

        else:
            self.exibir_mensagem_erro("Digite o nome do autor.")
    
    def exibir_resultado_busca(self, autor):
        resultado = f"Nome: {autor.get_nome()}\n" \
                    f"Nacionalidade: {autor.get_nacionalidade()}\n" \
                    f"Data de nascimento: {autor.get_data_nascimento()}"

        self.label_mensagem.config(text=resultado, fg="black")

    def voltar_para_tela_autor(self, janela_atual):
        janela_atual.destroy()
        self.janela_autor.deiconify()
