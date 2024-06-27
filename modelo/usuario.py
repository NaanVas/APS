class Usuario:
    def __init__(self, cpf, nome, senha, tipo):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.tipo = tipo #'admin' administrador, 'user' usuario

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha
    
    def get_tipo(self):
        return self.tipo
    
    def is_adm(self):
        return self.tipo == 'admin'
        