from entidade import EntidadeAcademica
from curso import Curso

class Campus(EntidadeAcademica):
    def __init__(self, codigo, nome, cidade):
        super().__init__(codigo, nome)
        self.cidade = cidade
        self.cursos = []  # lista de objetos Curso

    # ----- CRUD de CURSOS (dentro do campus) -----

    def adicionar_curso(self, curso):
        if not isinstance(curso, Curso):
            raise TypeError("Só é possível adicionar instâncias de Curso ao campus.")
        self.cursos.append(curso)

    def buscar_curso(self, codigo):
        # opcional: garantir que o código seja string
        if not isinstance(codigo, str):
            raise TypeError("O código de curso deve ser uma string (ex: 'SI', 'MED').")
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def remover_curso(self, codigo):
        curso = self.buscar_curso(codigo)
        if curso:
            self.cursos.remove(curso)
            return True
        return False

    def listar_cursos(self):
        return self.cursos

    def atualizar(self, novo_nome=None, nova_cidade=None):
        super().atualizar(novo_nome)
        if nova_cidade:
            self.cidade = nova_cidade

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.cidade})"
