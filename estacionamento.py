from vaga import Vaga

class Estacionamento:
    def __init__(self):
        self.vagas = [Vaga(i+1) for i in range(4)]

    def mostrar_status(self):
        for vaga in self.vagas:
            print(f"Vaga {vaga.numero}: {vaga.estado}")

    def alterar_estado(self, numero, novo_estado):
        vaga = self.vagas[numero-1]
        if novo_estado == "livre":
            vaga.liberar()
        elif novo_estado == "ocupada":
            vaga.ocupar()
        elif novo_estado == "reservada":
            vaga.reservar()
