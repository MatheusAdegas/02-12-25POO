# 1. Objetivo do projeto

Este projeto implementa um sistema simples em Python para gerenciar campi da UFC e seus cursos, usando listas e Programação Orientada a Objetos. É possível realizar operações de CRUD (criar, listar, atualizar e remover) tanto de campus quanto de cursos por meio de um menu interativo no terminal. Agora, o código também utiliza herança: uma classe base EntidadeAcademica concentra os atributos e comportamentos comuns (codigo, nome, atualizar, __str__), que são reaproveitados por Campus e Curso.

# 2. Estrutura de arquivos do projeto
```
projeto_ufc/
-> entidade.py        # classe base EntidadeAcademica
-> curso.py           # herda de EntidadeAcademica
-> campus.py          # herda de EntidadeAcademica e gerencia cursos
-> universidade.py    # gerencia a lista de campi (UFC)
-> sys.py             # menu principal e menu de cursos (interface via terminal)
```

Para executar o sistema, basta rodar o arquivo sys.py e utilizar as opções numéricas exibidas no menu para cadastrar, listar, atualizar e remover campi, além de gerenciar os cursos de cada campus.

3. Herança aplicada no código

A classe EntidadeAcademica define o básico que é comum a campus e curso:
```
# entidade.py
class EntidadeAcademica:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def atualizar(self, novo_nome=None):
        if novo_nome:
            self.nome = novo_nome

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
```

O Curso herda de EntidadeAcademica e adiciona o atributo tipo:

```
# curso.py
from entidade import EntidadeAcademica

class Curso(EntidadeAcademica):
    def __init__(self, codigo, nome, tipo):
        super().__init__(codigo, nome)
        self.tipo = tipo

    def atualizar(self, novo_nome=None, novo_tipo=None):
        super().atualizar(novo_nome)
        if novo_tipo:
            self.tipo = novo_tipo

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.tipo})"
```

O Campus também herda de EntidadeAcademica, adiciona cidade e a lista de cursos, e oferece o CRUD de cursos:

```
# campus.py
from entidade import EntidadeAcademica
from curso import Curso

class Campus(EntidadeAcademica):
    def __init__(self, codigo, nome, cidade):
        super().__init__(codigo, nome)
        self.cidade = cidade
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def buscar_curso(self, codigo):
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
```

O restante do sistema (menus em sys.py e gerenciamento de campi em universidade.py) continua funcionando como antes, apenas passando a usar os métodos atualizar herdados para modificar campus e cursos de forma mais reaproveitável.