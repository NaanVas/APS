import tkinter as tk
from tkinter import ttk
from controle.livro_controller import LivroController


class TelaLivro:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback
        self.livro_c = LivroController()
        self.janela_listar_aberta = False

        self.janela_livro = tk.Toplevel(self.root)
        self.janela_livro.title("Gerenciamento de Livros")
        self.janela_livro.geometry("450x300")
        self.janela_livro.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150 
        pos_y = 150 
        self.janela_livro.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_livro.focus_set()

        label_titulo = tk.Label(self.janela_livro, text="Tela de Gerenciamento de Livros", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        botao_cadastrar = ttk.Button(self.janela_livro, text="Cadastrar Livro", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.pack(pady=10)

        botao_excluir = ttk.Button(self.janela_livro, text="Excluir Livro", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.pack(pady=10)

        botao_buscar = ttk.Button(self.janela_livro, text="Buscar Livro", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.pack(pady=10)

        botao_listar = ttk.Button(self.janela_livro, text="Listar Livros", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_livro, text="Voltar", style="Estilo.TButton", command=self.fechar_tela_livro)
        botao_voltar.pack(pady=10)

        self.janela_livro.protocol("WM_DELETE_WINDOW", self.fechar_tela_livro)
        
    def fechar_tela_livro(self):
        self.janela_livro.destroy()
        self.voltar_callback()
    
    def abrir_tela_cadastrar(self):
        self.janela_livro.withdraw()

        self.janela_cadastrar = tk.Toplevel(self.janela_livro)
        self.janela_cadastrar.title("Cadastrar Livro")
        self.janela_cadastrar.geometry("300x470")
        self.janela_cadastrar.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
        self.janela_cadastrar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_cadastrar.focus_set()

    
        label_titulo = tk.Label(self.janela_cadastrar, text="Cadastrar Livro", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        tk.Label(self.janela_cadastrar, text="Título:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_titulo = tk.Entry(self.janela_cadastrar)
        self.entry_titulo.pack(pady=5)

        tk.Label(self.janela_cadastrar, text="Autor:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_autor = tk.Entry(self.janela_cadastrar)
        self.entry_autor.pack(pady=5)

        tk.Label(self.janela_cadastrar, text="Editora:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_editora = tk.Entry(self.janela_cadastrar)
        self.entry_editora.pack(pady=5)

        tk.Label(self.janela_cadastrar, text="Ano de Publicação:",font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_ano = tk.Entry(self.janela_cadastrar)
        self.entry_ano.pack(pady=5)

        self.label_mensagem = tk.Label(self.janela_cadastrar, text="",font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_salvar = ttk.Button(self.janela_cadastrar, text="Salvar", style="Estilo.TButton", command=self.salvar_livro)
        botao_salvar.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_cadastrar, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_livro(self.janela_cadastrar))
        botao_voltar.pack(pady=10)

        self.janela_cadastrar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_livro(self.janela_cadastrar))

    def salvar_livro(self):
        titulo = self.entry_titulo.get()
        autor_nome = self.entry_autor.get()
        editora = self.entry_editora.get()
        ano_publicacao = self.entry_ano.get()
        
        if titulo and autor_nome and editora and ano_publicacao:
            resultado = self.livro_c.cadastrar_livro(titulo, autor_nome, editora, ano_publicacao)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Livro '{titulo}' cadastrado com sucesso.")
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
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_titulo.focus_set()

    def abrir_tela_excluir(self):
        self.janela_livro.withdraw()

        self.janela_excluir = tk.Toplevel(self.root)
        self.janela_excluir.title("Excluir Livro")
        self.janela_excluir.geometry("400x300")
        self.janela_excluir.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
    
        self.janela_excluir.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_excluir.focus_set()


        label_titulo = tk.Label(self.janela_excluir, text="Excluir Livro", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        entry_titulo = tk.Entry(self.janela_excluir)
        entry_titulo.pack(pady=10)

        self.label_mensagem = tk.Label(self.janela_excluir, text="",font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)


        botao_excluir = ttk.Button(self.janela_excluir, text="Excluir", style="Estilo.TButton", command=lambda: self.excluir_livro(entry_titulo.get()))
        botao_excluir.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_excluir, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_livro(self.janela_excluir))
        botao_voltar.pack(pady=10)

        self.janela_excluir.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_livro(self.janela_excluir))

    def excluir_livro(self, titulo):
        resultado = self.livro_c.excluir_livro(titulo)
        if resultado is None:
            self.exibir_mensagem_sucesso(f"Livro '{titulo}' excluído com sucesso.")

            if self.janela_listar_aberta:
                self.abrir_tela_listar()
        else:
            self.exibir_mensagem_erro(resultado)


    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar.destroy()
        self.janela_listar_aberta = True
        livros = self.livro_c.listar_livros()

        self.janela_listar = tk.Toplevel(self.root)
        self.janela_listar.title("Listagem de Livros")
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

        # Text widget para exibir os livros com scrollbar
        text_area = tk.Text(self.janela_listar, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#F0DAAE", font=("Montserrat", 10))
        text_area.pack(fill=tk.BOTH, expand=True)

        # Configurar a scrollbar para interagir com o widget de texto
        scrollbar.config(command=text_area.yview)

        # Escrever os livros no widget de texto
        for livro in livros:
            titulo = f"Título: {livro.get_titulo()}\n"
            autor = f"Autor: {livro.get_autor()}\n"
            editora = f"Editora: {livro.get_editora()}\n"
            ano = f"Ano de Publicação: {livro.get_ano_publicacao()}\n\n"

            # Inserir texto formatado com tags de estilo no tkinter
            text_area.insert(tk.END, titulo, "negrito")
            text_area.insert(tk.END, autor)
            text_area.insert(tk.END, editora)
            text_area.insert(tk.END, ano)

            text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))

        self.janela_listar.protocol("WM_DELETE_WINDOW", self.fechar_janela_listar)

    def fechar_janela_listar(self):
        self.janela_listar_aberta = False
        self.janela_listar.destroy()
    
    def atualizar_lista_livros(self):
        livros = self.livro_c.listar_livros()
        if self.janela_listar_aberta:
            self.text_area.delete(1.0, tk.END)  # Limpar o conteúdo atual do widget de texto

            for livro in livros:
                titulo = f"Título: {livro.get_titulo()}\n"
                autor = f"Autor: {livro.get_autor()}\n"
                editora = f"Editora: {livro.get_editora()}\n"
                ano = f"Ano de Publicação: {livro.get_ano_publicacao()}\n\n"

                # Inserir texto formatado com tags de estilo no tkinter
                self.text_area.insert(tk.END, titulo, "negrito")
                self.text_area.insert(tk.END, autor)
                self.text_area.insert(tk.END, editora)
                self.text_area.insert(tk.END, ano)

            # Atualizar a barra de rolagem
            self.text_area.config(state=tk.DISABLED)  # Desativar edição para permitir rolagem
            self.text_area.yview(tk.END)  # Rolar para o final do texto
        
    def abrir_tela_buscar(self):
        self.janela_buscar = tk.Toplevel(self.janela_livro)
        self.janela_buscar.title("Buscar Livro")
        self.janela_buscar.geometry("400x200")
        self.janela_buscar.configure(bg="#F0DAAE")
        largura = 600
        altura = 470
        pos_x = 150  
        pos_y = 150  
        self.janela_buscar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_buscar.focus_set()

        label_titulo = tk.Label(self.janela_buscar, text="Buscar Livro", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        tk.Label(self.janela_buscar, text="Título:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_busca_titulo = tk.Entry(self.janela_buscar)
        self.entry_busca_titulo.pack(pady=5)

        botao_buscar = ttk.Button(self.janela_buscar, text="Buscar", style="Estilo.TButton", command=self.buscar_livro)
        botao_buscar.pack(pady=10)

        self.label_mensagem = tk.Label(self.janela_buscar, text="", font=("Montserrat", 10), fg="red", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_buscar, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_livro(self.janela_buscar))
        botao_voltar.pack(pady=10)

        self.janela_buscar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_livro(self.janela_buscar))

    def buscar_livro(self):
        titulo = self.entry_busca_titulo.get()
        if titulo:
            livro = self.livro_c.buscar_livro(titulo)
            if livro:
                self.exibir_resultado_busca(livro)
                self.entry_busca_titulo.delete(0, tk.END)
                self.entry_busca_titulo.focus_set()


            else:
                self.exibir_mensagem_erro(f"Livro '{titulo}' não encontrado.")
                self.entry_busca_titulo.delete(0, tk.END)
                self.entry_busca_titulo.focus_set()

        else:
            self.exibir_mensagem_erro("Digite o título do livro.")
    
    def exibir_resultado_busca(self, livro):
        resultado = f"Título: {livro.get_titulo()}\n" \
                    f"Autor: {livro.get_autor()}\n" \
                    f"Editora: {livro.get_editora()}\n" \
                    f"Ano de Publicação: {livro.get_ano_publicacao()}"

        self.label_mensagem.config(text=resultado, fg="black")

    def voltar(self):
        self.janela_livro.destroy()
        self.voltar_callback()

    def voltar_para_tela_livro(self, janela_atual):
        janela_atual.destroy()
        self.janela_livro.deiconify()
