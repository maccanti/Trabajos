def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron {cantidad} unidades en la cuenta.")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")