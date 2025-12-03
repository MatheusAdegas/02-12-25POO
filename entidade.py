# entidade.py
class EntidadeAcademica:
    def __init__(self, codigo, nome):
        # não vou forçar tipo específico de codigo aqui,
        # mas posso garantir que nome é string
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        self.codigo = codigo
        self.nome = nome

    def atualizar(self, novo_nome=None):
        if novo_nome is not None:
            if not isinstance(novo_nome, str):
                raise TypeError("O novo nome deve ser uma string.")
            if novo_nome.strip() != "":
                self.nome = novo_nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
