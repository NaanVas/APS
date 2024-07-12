class Usuario:
    def __init__(self, cpf, nome, senha, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.data_nascimento = data_nascimento

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

    def get_data_nascimento(self):
        return self.data_nascimento
    
    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
