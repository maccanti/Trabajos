longitud = int(input("Ingresa la longitud de la lista: "))
minimo = int(input("Ingresa el valor mínimo: "))
maximo = int(input("Ingresa el valor máximo: "))

import random

def generar_lista_aleatoria(longitud, minimo, maximo):
    lista_aleatoria = [random.randint(minimo, maximo) for _ in range(longitud)]
    return lista_aleatoria

print("La lista aleatoria es:",generar_lista_aleatoria)