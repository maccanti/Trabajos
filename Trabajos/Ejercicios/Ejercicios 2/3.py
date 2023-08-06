class Punto():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def coordenadas(self):
        return f'({self.x}, {self.y})'
    def mover_coordenadas(self, x2, y2):
        self.x += x2
        self.y += y2
    def distancia_puntos(self, punto2):
        x2=self.x-punto2.x
        y2=self.y-punto2.y
        return(x2**2+y2**2)**0.5



punto1 = Punto(2, 3)
punto2 = Punto(5, 7)

print("Coordenadas del punto 1:", punto1)
print("Coordenadas del punto 2:", punto2)
print("Distancia entre los puntos:", punto1.distancia_puntos(punto2))

punto1.mover_coordenadas(1, -2)
print("Nuevas coordenadas del punto 1:", punto1)
