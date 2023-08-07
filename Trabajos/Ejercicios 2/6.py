class Carta:
    PINTAS = ("Corazón", "Diamante", "Trébol", "Pica")

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


valor_carta = "10"
pinta_carta = Carta.PINTAS[0] 
carta = Carta(valor_carta, pinta_carta)

print("Valor de la carta:", carta.valor)
print("Pinta de la carta:", carta.pinta)