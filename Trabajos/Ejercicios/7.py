numeros_str = input(str("Ingresa los números separados por espacios: "))
numeros_lista = [int(x) for x in numeros_str.split()]

def encontrar_extremos_lista(lista):
    if len(lista) == 0:
        return None, None  

    minimo = maximo = lista[0]  

    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero

    return minimo, maximo

minimo, maximo = encontrar_extremos_lista(numeros_lista)

if minimo is None:
    print("La lista está vacía.")
else:
    print("El número más pequeño en la lista es:", minimo)
    print("El número más grande en la lista es:", maximo)