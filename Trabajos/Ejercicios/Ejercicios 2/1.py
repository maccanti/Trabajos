class Vehiculo():
    def __init__(self, tipo, velocidad_maxima, kilometraje):
        self.tipo = tipo
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
    def correr(self):
        print("El/La", self.tipo,"alcanza una gran velocidad")
    def recorrer(self):
        print("El/la", self.tipo,"ha recorrido",self.kilometraje,"Kilometros")

mi_vehiculo = Vehiculo("moto", 90, 200)
print("Mi vehiculo es una",str(mi_vehiculo.tipo),".")
print("Mi",mi_vehiculo.tipo,"va a", float(mi_vehiculo.velocidad_maxima),"Km/h")
mi_vehiculo.correr()
mi_vehiculo.recorrer()