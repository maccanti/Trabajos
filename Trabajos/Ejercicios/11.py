def generar_numeros_pares(inicio, fin):
    numeros_pares = []
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares

numeros_pares = generar_numeros_pares(1, 100)
print(numeros_pares)