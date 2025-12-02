from entidade import EntidadeAcademica

class Curso(EntidadeAcademica):
    def __init__(self, codigo, nome, tipo):
        super().__init__(codigo, nome)  # inicializa codigo e nome na classe base
        self.tipo = tipo

    def atualizar(self, novo_nome=None, novo_tipo=None):
        # reaproveita a lógica de atualizar nome da classe base
        super().atualizar(novo_nome)

        if novo_tipo:
            self.tipo = novo_tipo

    def __str__(self):
        # acrescenta o tipo na string
        return f"{self.codigo} - {self.nome} ({self.tipo})"