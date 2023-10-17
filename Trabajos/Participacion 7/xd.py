from dataclasses import dataclass

@dataclass
class Elemento:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        for e in self.elementos:
            if e == elemento:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        interseccion_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        interseccion_elementos = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nuevo_conjunto = Conjunto(interseccion_nombre)
        for elemento in interseccion_elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"
