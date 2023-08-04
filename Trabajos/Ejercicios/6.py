numeros_str = input(str("Ingresa los números separados por espacios: "))
numeros_lista = [int(x) for x in numeros_str.split()]

def calcular_suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print("La suma de los números en la lista es:", calcular_suma_lista)