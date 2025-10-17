class Vaga:
    def __init__(self, numero):
        self.numero = numero
        self.estado = "Livre"

    def ocupar(self):
        self.estado = "Ocupada"

    def liberar(self):
        self.estado = "Livre"

    def reservar(self):
        self.estado = "Reservada"
