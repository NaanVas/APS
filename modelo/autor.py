class Autor:
    def __init__(self, nome, nacionalidade, data_nascimento):
        self.set_nome(nome)
        self.set_nacionalidade(nacionalidade)
        self.set_data_nascimento(data_nascimento)

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_nacionalidade(self):
        return self._nacionalidade

    def set_nacionalidade(self, nova_nacionalidade):
        self._nacionalidade = nova_nacionalidade

    def get_data_nascimento(self):
        return self._data_nascimento

    def set_data_nascimento(self, nova_data):
        self._data_nascimento = nova_data
    