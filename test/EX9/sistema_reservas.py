class Voo:
    def __init__(self, numero_voo, origem, destino, data, horario):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self.data = data
        self.horario = horario

class Reserva:
    def __init__(self, voo, passageiro):
        self.voo = voo
        self.passageiro = passageiro

class SistemaReservas:
    def __init__(self):
        self.voos = []
        self.reservas = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def realizar_reserva(self, numero_voo, passageiro):
        for voo in self.voos:
            if voo.numero_voo == numero_voo:
                reserva = Reserva(voo, passageiro)
                self.reservas.append(reserva)
                return reserva
        return None

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
            return True
        return False
