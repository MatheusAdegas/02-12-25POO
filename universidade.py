from campus import Campus

class UFC:
    def __init__(self):
        self.campi = []  # lista de objetos Campus
        
    def adicionar_campus(self, campus):
        if not isinstance(campus, Campus):
            raise TypeError("Só é possível adicionar instâncias de Campus à UFC.")
        self.campi.append(campus)

    def buscar_campus(self, codigo):
        # aqui você espera um int
        if not isinstance(codigo, int):
            raise TypeError("O código do campus deve ser um número inteiro.")
        for campus in self.campi:
            if campus.codigo == codigo:
                return campus
        return None

    def remover_campus(self, codigo):
        campus = self.buscar_campus(codigo)
        if campus:
            self.campi.remove(campus)
            return True
        return False

    def listar_campi(self):
        return self.campi
