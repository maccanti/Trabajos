class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance


numero_cuenta = "123456789"
propietarios = ["Alice", "Bob"]
balance = 1000.0
cuenta = CuentaBancaria(numero_cuenta, propietarios, balance)

print("Número de cuenta:", cuenta.numero_cuenta)
print("Propietarios:", cuenta.propietarios)
print("Balance:", cuenta.balance)