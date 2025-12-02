class EntidadeAcademica:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def atualizar(self, novo_nome=None):
        if novo_nome:
            self.nome = novo_nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


