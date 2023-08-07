def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron {cantidad} unidades de la cuenta.")
        else:
            print("Cantidad inválida para el retiro o saldo insuficiente.")