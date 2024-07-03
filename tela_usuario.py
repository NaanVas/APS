import tkinter as tk
from tkinter import ttk
from controle.usuario_controller import UsuarioController

class TelaUsuario:
    def __init__(self, root, voltar_callback):
        self.root = root
        self.voltar_callback = voltar_callback
        self.usuario_controller = UsuarioController()
        self.janela_listar_aberta = False

        self.janela_usuario = tk.Toplevel(self.root)
        self.janela_usuario.title("Gerenciamento de Usuários")
        self.root.geometry("600x450")
        self.janela_usuario.configure(bg="#F0DAAE")
        largura = 600
        altura = 450
        pos_x = 150  
        pos_y = 150  
        self.janela_usuario.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_usuario.focus_set()

        label_titulo = tk.Label(self.janela_usuario, text="Tela de Gerenciamento de Usuários", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        botao_cadastrar = ttk.Button(self.janela_usuario, text="Cadastrar Usuário", style="Estilo.TButton", command=self.abrir_tela_cadastrar)
        botao_cadastrar.pack(pady=10)

        botao_excluir = ttk.Button(self.janela_usuario, text="Excluir Usuário", style="Estilo.TButton", command=self.abrir_tela_excluir)
        botao_excluir.pack(pady=10)

        botao_buscar = ttk.Button(self.janela_usuario, text="Buscar Usuário", style="Estilo.TButton", command=self.abrir_tela_buscar)
        botao_buscar.pack(pady=10)

        botao_listar = ttk.Button(self.janela_usuario, text="Listar Usuários", style="Estilo.TButton", command=self.abrir_tela_listar)
        botao_listar.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_usuario, text="Voltar", style="Estilo.TButton", command=self.fechar_tela_usuario)
        botao_voltar.pack(pady=10)

        self.janela_usuario.protocol("WM_DELETE_WINDOW", self.fechar_tela_usuario)
        
    def fechar_tela_usuario(self):
        self.janela_usuario.destroy()
        self.voltar_callback()
    
    def abrir_tela_cadastrar(self):
        self.janela_usuario.withdraw()

        self.janela_cadastrar = tk.Toplevel(self.janela_usuario)
        self.janela_cadastrar.title("Cadastrar Usuário")
        self.janela_cadastrar.geometry("600x450+150+150")
        self.janela_cadastrar.configure(bg="#F0DAAE")
        self.janela_cadastrar.focus_set()

        frame_central = tk.Frame(self.janela_cadastrar, bg="#F0DAAE")
        frame_central.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_titulo = tk.Label(frame_central, text="Cadastrar Usuário", font=("Montserrat", 16, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame_central, text="CPF:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=1, column=0, pady=5, sticky='e', padx=15)
        self.entry_cpf = tk.Entry(frame_central)
        self.entry_cpf.grid(row=1, column=1, pady=5)

        tk.Label(frame_central, text="Nome:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=2, column=0, pady=5, sticky='e')
        self.entry_nome = tk.Entry(frame_central)
        self.entry_nome.grid(row=2, column=1, pady=5)

        tk.Label(frame_central, text="Senha:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").grid(row=3, column=0, pady=5, sticky='e')
        self.entry_senha = tk.Entry(frame_central, show="*")
        self.entry_senha.grid(row=3, column=1, pady=5)

        self.is_admin = tk.BooleanVar()
        check_admin = tk.Checkbutton(frame_central, text="Administrador", variable=self.is_admin, font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE", command=self.toggle_salario_entry)
        check_admin.grid(row=4, column=0, columnspan=2, pady=5)

        self.label_salario = tk.Label(frame_central, text="Salário:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE")
        self.entry_salario = tk.Entry(frame_central)

        self.label_mensagem = tk.Label(frame_central, text="", font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.grid(row=5, column=0, columnspan=2, pady=10)

        botao_salvar = ttk.Button(frame_central, text="Salvar", style="Estilo.TButton", command=self.salvar_usuario)
        botao_salvar.grid(row=6, column=0, pady=10)

        botao_voltar = ttk.Button(frame_central, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_usuario(self.janela_cadastrar))
        botao_voltar.grid(row=6, column=1, pady=10)

        self.janela_cadastrar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_usuario(self.janela_cadastrar))


    def toggle_salario_entry(self):
        if self.is_admin.get():
            self.label_salario.grid(row=7, column=0, pady=5)
            self.entry_salario.grid(row=7, column=1, pady=5)
            self.label_mensagem.grid(row=8, column=0, columnspan=2, pady=10)
            self.botao_salvar.grid(row=9, column=0, pady=10)
        else:
            self.label_salario.grid_remove()
            self.entry_salario.grid_remove()
            self.label_mensagem.grid(row=5, column=0, columnspan=2, pady=10)
            self.botao_salvar.grid(row=6, column=0, pady=10)

    def salvar_usuario(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        tipo = 'admin' if self.is_admin.get() else 'user'
        salario = self.entry_salario.get() if self.is_admin.get() else None

        if cpf and nome and senha:
            resultado = self.usuario_controller.cadastrar_usuario(cpf, nome, senha, tipo, salario)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Usuário '{nome}' cadastrado com sucesso.")
                self.limpar_campos()

                if self.janela_listar_aberta:
                    self.abrir_tela_listar()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Todos os campos são obrigatórios.")

    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.is_admin.set(False)
        self.entry_salario.delete(0, tk.END)
        self.toggle_salario_entry()
        self.entry_cpf.focus_set()

    def exibir_mensagem_sucesso(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="green")

    def exibir_mensagem_erro(self, mensagem):
        self.label_mensagem.config(text=mensagem, fg="red")


    def abrir_tela_excluir(self):
        self.janela_usuario.withdraw()

        self.janela_excluir = tk.Toplevel(self.root)
        self.janela_excluir.title("Excluir Usuário")
        self.root.geometry("600x450")
        self.janela_excluir.configure(bg="#F0DAAE")
        largura = 600
        altura = 450
        pos_x = 150  
        pos_y = 150  
        self.janela_excluir.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_excluir.focus_set()

        label_titulo = tk.Label(self.janela_excluir, text="Excluir Usuário", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        tk.Label(self.janela_excluir, text="CPF:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_excluir_cpf = tk.Entry(self.janela_excluir)
        self.entry_excluir_cpf.pack(pady=5)

        self.label_mensagem = tk.Label(self.janela_excluir, text="", font=("Montserrat", 8), fg="#482E1D", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_excluir = ttk.Button(self.janela_excluir, text="Excluir", style="Estilo.TButton", command=self.excluir_usuario)
        botao_excluir.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_excluir, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_usuario(self.janela_excluir))
        botao_voltar.pack(pady=10)

        self.janela_excluir.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_usuario(self.janela_excluir))

    def excluir_usuario(self):
        cpf = self.entry_excluir_cpf.get()
        if cpf:
            resultado = self.usuario_controller.excluir_usuario(cpf)
            if resultado is None:
                self.exibir_mensagem_sucesso(f"Usuário com CPF '{cpf}' excluído com sucesso.")

                if self.janela_listar_aberta:
                    self.abrir_tela_listar()
            else:
                self.exibir_mensagem_erro(resultado)
        else:
            self.exibir_mensagem_erro("Digite o CPF do usuário.")

    def abrir_tela_listar(self):
        if self.janela_listar_aberta:
            self.janela_listar.destroy()
        self.janela_listar_aberta = True
        usuarios = self.usuario_controller.listar_usuarios()

        self.janela_listar = tk.Toplevel(self.root)
        self.janela_listar.title("Listagem de Usuários")
        self.root.geometry("600x450")
        self.janela_listar.configure(bg="#F0DAAE")
        largura = 600
        altura = 450
        largura_tela = self.janela_listar.winfo_screenwidth()
        pos_x = largura_tela - largura - 150  
        pos_y = 150  
        self.janela_listar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_listar.focus_set()

        # Configurar scrollbar
        scrollbar = tk.Scrollbar(self.janela_listar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget para exibir os usuários com scrollbar
        text_area = tk.Text(self.janela_listar, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#F0DAAE", font=("Montserrat", 10))
        text_area.pack(fill=tk.BOTH, expand=True)

        # Configurar a scrollbar para interagir com o widget de texto
        scrollbar.config(command=text_area.yview)

        # Escrever os usuários no widget de texto
        for usuario in usuarios:
            cpf = f"CPF: {usuario.get_cpf()}\n"
            nome = f"Nome: {usuario.get_nome()}\n"
            tipo = f"Tipo: {usuario.get_tipo()}\n"

            # Inserir texto formatado com tags de estilo no tkinter
            text_area.insert(tk.END, cpf, "negrito")
            text_area.insert(tk.END, nome)
            text_area.insert(tk.END, tipo)

            text_area.tag_configure("negrito", font=("Montserrat", 10, "bold"))

        self.janela_listar.protocol("WM_DELETE_WINDOW", self.fechar_janela_listar)

    def fechar_janela_listar(self):
        self.janela_listar_aberta = False
        self.janela_listar.destroy()
    
    def abrir_tela_buscar(self):
        self.janela_buscar = tk.Toplevel(self.janela_usuario)
        self.janela_buscar.title("Buscar Usuário")
        self.root.geometry("600x450")
        self.janela_buscar.configure(bg="#F0DAAE")
        largura = 600
        altura = 450
        pos_x = 150  
        pos_y = 150  
        self.janela_buscar.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.janela_buscar.focus_set()

        label_titulo = tk.Label(self.janela_buscar, text="Buscar Usuário", font=("Montserrat", 18, "bold"), fg="#482E1D", bg="#F0DAAE")
        label_titulo.pack(pady=20)

        tk.Label(self.janela_buscar, text="CPF:", font=("Montserrat", 10), fg="#482E1D", bg="#F0DAAE").pack(pady=5)
        self.entry_busca_cpf = tk.Entry(self.janela_buscar)
        self.entry_busca_cpf.pack(pady=5)

        botao_buscar = ttk.Button(self.janela_buscar, text="Buscar", style="Estilo.TButton", command=self.buscar_usuario)
        botao_buscar.pack(pady=10)

        self.label_mensagem = tk.Label(self.janela_buscar, text="", font=("Montserrat", 10), fg="red", bg="#F0DAAE")
        self.label_mensagem.pack(pady=10)

        botao_voltar = ttk.Button(self.janela_buscar, text="Voltar", style="Estilo.TButton", command=lambda: self.voltar_para_tela_usuario(self.janela_buscar))
        botao_voltar.pack(pady=10)

        self.janela_buscar.protocol("WM_DELETE_WINDOW", lambda: self.voltar_para_tela_usuario(self.janela_buscar))

    def buscar_usuario(self):
        cpf = self.entry_busca_cpf.get()
        if cpf:
            usuario = self.usuario_controller.buscar_usuario(cpf)
            if usuario:
                self.exibir_resultado_busca(usuario)
                self.entry_busca_cpf.delete(0, tk.END)
                self.entry_busca_cpf.focus_set()
            else:
                self.exibir_mensagem_erro(f"Usuário com CPF '{cpf}' não encontrado.")
                self.entry_busca_cpf.delete(0, tk.END)
                self.entry_busca_cpf.focus_set()
        else:
            self.exibir_mensagem_erro("Digite o CPF do usuário.")

    def exibir_resultado_busca(self, usuario):
        resultado = f"CPF: {usuario.get_cpf()}\n" \
                    f"Nome: {usuario.get_nome()}\n" \
                    f"Tipo: {usuario.get_tipo()}\n" \
                    f"Tipo: {usuario.get_tipo()}"

        self.label_mensagem.config(text=resultado, fg="black")

    def voltar(self):
        self.janela_usuario.destroy()
        self.voltar_callback()

    def voltar_para_tela_usuario(self, janela_atual):
        janela_atual.destroy()
        self.janela_usuario.deiconify()